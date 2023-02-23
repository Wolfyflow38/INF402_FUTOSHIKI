module futoshiki;

import std.algorithm : map;
import std.typecons : Ternary, Tuple;
import std.conv : to, ConvException;
import std.array : join, array;
import std.format : format;
import std.format.spec : singleSpec;
import std.format.read : unformatValue, formattedRead;
import std.stdio : stdin, stdout, File, lines, stderr;
import std.regex : ctRegex, regex, matchAll;
import std.file : readText;
import std.json : parseJSON, JSONValue, JSONType;

class table {
    @disable this();

    immutable ulong n;
    ulong [][] values;
    Ternary [][] h_sign;
    Ternary [][] v_sign;

    invariant(values.length == n);
    invariant(h_sign.length == n - 1);
    invariant(v_sign.length == n);

    this(ulong n) in(n > 0){
        this.n = n;
        values = new ulong[][](n,n);
        h_sign = new Ternary[][](n-1, n);
        v_sign = new Ternary[][](n, n-1);
    }

    this(string f) {
        const(JSONValue) v = parseJSON(f);
        this(cast(ulong)v["size"].integer);
        if (const(JSONValue)* value = "value" in v) {
            for(ulong x = 0; x < n; x+=1) {
                string x_s = x.to!string;
                for(ulong y = 0; y < n; y+=1) {
                    string s = x_s ~ ":" ~y.to!string;
                    if(const(JSONValue)* t = s in *value) {
                        final switch (t.type) {
                            case JSONType.null_: {

                            } break;
                            case JSONType.string : {
                                string ts = t.str;
                                if(ts == "*") {
                                    break;
                                } else {
                                    try {
                                        set_value_at(x, y, ts.to!ulong);
                                    } catch (ConvException e) {
                                        assert(0);
                                    }
                                }
                            } break;
                            case JSONType.integer,
                            JSONType.uinteger: {
                                set_value_at(x, y, t.type == JSONType.integer ? cast(ulong) t.integer : t.uinteger);
                            } break;
                            case JSONType.object,
                            JSONType.float_,
                            JSONType.true_,
                            JSONType.false_,
                            JSONType.array: assert(0);
                        }
                    }
                }
            }
        }
    }

    void set_h_sign_at(ulong x, ulong y, Ternary t) in(x < (n - 1) && y < n) {
        h_sign[x][y] = t;
    }

    void set_v_sign_at(ulong x, ulong y, Ternary t) in(x < n && y < (n - 1)) {
        v_sign[x][y] = t;
    }

    void set_value_at(ulong x, ulong y, ulong v) in(v < n && x < n && y < n) {
        values[x][y] = v;
    }

    ulong gen_id_for(ulong x, ulong y, ulong v) const out(rv; rv <= n*n*n)  {
        return x*n*n + y*n + v;
    }

    string[] gen_c_clauses() const {
        string [] rv = [];
        for(ulong x = 0; x < n; x+=1)
        for(ulong y = 0; y < n; y+=1)
        if(values[x][y] != 0){
            for(ulong v1 = 0; v1 < n; v1+=1) {
                if((v1+1) == values[x][y]) {
                    rv ~= to!string(gen_id_for(x, y, v1+1)) ~ " 0";
                } else {
                    rv ~= "-" ~ to!string(gen_id_for(x, y, v1+1)) ~ " 0";
                }
            }
        }else {
            string[] s = [];
            for(ulong v1 = 0; v1 < n; v1+=1) {
                string v = to!string(gen_id_for(x, y, v1+1));
                s ~= v;
                for(ulong v2 = v1 + 1; v2 < n; v2+=1) {
                    rv ~= "-" ~ v ~ " -" ~ to!string(gen_id_for(x, y, v2+1)) ~ " 0";
                }
            }
            rv ~= join(s, " ") ~ " 0";
        }
        return rv;
    }

    string[] gen_v_clauses() const {
        alias tp = Tuple!(
            string[], "search",
            bool, "exist",
            string[], "single",
            string[], "exclude",
            string, "force"
        );
        tp [] rv = [];
        for(ulong x = 0; x < n; x+=1) {
            tp [] trv = new tp[n];
            for(ulong y = 0; y < n; y+=1) {
                ulong val = values[x][y];
                for(ulong v = 1; v <= n; v += 1) {
                    string s = to!string(gen_id_for(x,y,v));
                    tp*p = &(trv[v-1]);
                    if(val == v) {
                        p.exist = true;
                        p.force = "-" ~ s ~ " 0";
                    } else {
                        p.search ~= s;
                        p.exclude ~= "-" ~ s;
                        for(ulong z = y; z < n; z += 1)
                            p.single ~= "-" ~ s ~ " -" ~ to!string(gen_id_for(x,z,v)) ~ " 0";
                    }
                }           
            }
            rv ~= trv;
        }
        return join(rv.map!(
            x => x.exist ? x.exclude ~ [x.force] : (x.single ~ join(x.search ~ "0", " "))
        )().array, new string[](0));
    }

    string[] gen_h_clauses() const {
        alias tp = Tuple!(
            string[], "search",
            bool, "exist",
            string[], "single",
            string[], "exclude",
            string, "force"
        );
        tp [] rv = [];
        for(ulong y = 0; y < n; y+=1) {
            tp [] trv = new tp[n];
            for(ulong x = 0; x < n; x+=1) {
                ulong val = values[x][y];
                for(ulong v = 1; v <= n; v += 1) {
                    string s = to!string(gen_id_for(x,y,v));
                    tp*p = &(trv[v-1]);
                    if(val == v) {
                        p.exist = true;
                        p.force = "-" ~ s ~ " 0";
                    } else {
                        p.search ~= s;
                        p.exclude ~= "-" ~ s;
                        for(ulong z = x; z < n; z += 1)
                            p.single ~= "-" ~ s ~ " -" ~ to!string(gen_id_for(z,y,v)) ~ " 0";
                    }
                }           
            }
            rv ~= trv;
        }
        return join(rv.map!(
            x => x.exist ? x.exclude ~ [x.force] : (x.single ~ [join(x.search ~ "0", " ")])
        )().array, new string[](0));
    }

    string[] gen_h_sign_clauses() const {
        string [] rv = [];

        return rv;
    }

    string[] gen_v_sign_clauses() const {
        string [] rv = [];

        return rv;
    }

    string gen_cnf() const {
        string[] c_clauses = gen_c_clauses();
        string[] v_clauses = gen_v_clauses();
        string[] h_clauses = gen_h_clauses();
        string[] v_sign_clauses = gen_v_sign_clauses();
        string[] h_sign_clauses = gen_h_sign_clauses();
        string[] all_clauses = c_clauses ~ v_clauses ~ h_clauses;
        return "p cnf " ~ to!string(n*n*n) ~ " " ~ to!string(all_clauses.length) ~ "\n" ~ join(all_clauses, "\n");
    }
}

int main(string[]s) {
    string str = "";
    if (s.length == 2) {
        str = readText(s[1]);
    } else {
        assert(s.length == 1);
        foreach(string line; lines(stdin)) str ~= line;
    }
    table t = new table(str);
    
    stdout.writeln(t.gen_cnf());

    return 0;
}