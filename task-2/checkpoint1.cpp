// Brute-force all 26 shifts for a lowercase-only Caesar cipher.

#include <bits/stdc++.h>
using namespace std;

string caesar_shift(const string &s, int shift)
{
    string out;
    out.reserve(s.size());
    for (char ch : s)
    {
        if (ch >= 'a' && ch <= 'z')
        {
            char p = char((ch - 'a' - shift + 26) % 26 + 'a');
            out.push_back(p);
        }
        else if (ch >= 'A' && ch <= 'Z')
        {
            char p = char((ch - 'A' - shift + 26) % 26 + 'A');
            out.push_back(p);
        }
        else
        {
            out.push_back(ch);
        }
    }
    return out;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const string cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo";

    cout << "Ciphertext: " << cipher << "\n\n";
    cout << "Trying all 26 shifts (shift = number of positions the cipher was shifted):\n\n";
    for (int shift = 0; shift < 26; ++shift)
    {
        cout << "Shift " << setw(2) << shift << ": " << caesar_shift(cipher, shift) << "\n";
    }
    
    return 0;
}
