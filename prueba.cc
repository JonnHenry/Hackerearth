#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t)
    {
        int n, i;
        cin >> n;
        int C[n], L[n];

        for (i = 0; i < n; i++)
        {
            cin >> C[i];
        }

        for (i = 0; i < n; i++)
        {
            cin >> L[i];
        }

        long minCost = 0, min = 999999, sum = 0;

        for (i = 0; i < n; i++)
        {
            if (C[i] < min)
            {
                min = C[i];
                sum = 0;
            }
            minCost = minCost + L[i] * min;
        }

        cout << minCost << endl;

        t--;
    }
}

