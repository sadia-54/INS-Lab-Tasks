#include <bits/stdc++.h>
using namespace std;

const string ENG_ORDER = "etaoinshrdlcumwfgypbvkjxqz";

const vector<string> COMMON_WORDS = {
    " the ", " and ", " of ", " to ", " a ", " in ", " is ", " that ", " it ", " as "};

// count letter frequencies in ciphertext
array<int, 26> count_freq(const string &s)
{
    array<int, 26> cnt{};
    cnt.fill(0);
    for (char c : s)
        if (c >= 'a' && c <= 'z')
            cnt[c - 'a']++;
    return cnt;
}

// generate initial key by frequency mapping
array<char, 26> initial_key(const string &cipher)
{
    auto cnt = count_freq(cipher);
    vector<int> idx(26);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int a, int b)
         { return cnt[a] > cnt[b]; });
    array<char, 26> key;
    for (int i = 0; i < 26; i++)
        key[idx[i]] = ENG_ORDER[i];
    return key;
}

// decrypt using given key
string decrypt(const array<char, 26> &key, const string &cipher)
{
    string out;
    out.reserve(cipher.size());
    for (char c : cipher)
    {
        if (c >= 'a' && c <= 'z')
            out.push_back(key[c - 'a']);
        else if (c >= 'A' && c <= 'Z')
            out.push_back(toupper(key[c - 'A']));
        else
            out.push_back(c);
    }
    return out;
}

// scoring function for English-likeness
int score(const string &plain)
{
    int s = 0;
    string t = plain;
    for (char &c : t)
        if (c >= 'A' && c <= 'Z')
            c = c - 'A' + 'a';
    for (auto &w : COMMON_WORDS)
    {
        size_t pos = 0;
        while ((pos = t.find(w, pos)) != string::npos)
        {
            s += 10;
            pos += w.size();
        }
    }
    for (char c : t)
        if (c == 'e' || c == 't' || c == 'a' || c == 'o' || c == 'n')
            s++;
    return s;
}

// hill climbing
string hill_climb(string cipher, int iterations = 5000)
{
    for (char &c : cipher)
        if (c >= 'A' && c <= 'Z')
            c = c - 'A' + 'a';

    array<char, 26> best_key = initial_key(cipher);
    string best_plain = decrypt(best_key, cipher);
    int best_score = score(best_plain);

    mt19937 rng((unsigned)chrono::high_resolution_clock::now().time_since_epoch().count());

    for (int t = 0; t < iterations; t++)
    {
        array<char, 26> cand = best_key;
        int i = rng() % 26, j = rng() % 26;
        swap(cand[i], cand[j]);

        string cand_plain = decrypt(cand, cipher);
        int cand_score = score(cand_plain);
        if (cand_score > best_score)
        {
            best_key = cand;
            best_plain = cand_plain;
            best_score = cand_score;
        }
    }
    return best_plain;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string cipher1 =
        "af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe";

    string cipher2 =
        "aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu-aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu-aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu";

    cout << "=== Decrypting Cipher 1 ===\n";
    string plain1 = hill_climb(cipher1);
    cout << plain1.substr(0, 1000) << "\n\n";

    cout << "=== Decrypting Cipher 2 ===\n";
    string plain2 = hill_climb(cipher2);
    cout << plain2.substr(0, 1000) << "\n";

    return 0;
}
