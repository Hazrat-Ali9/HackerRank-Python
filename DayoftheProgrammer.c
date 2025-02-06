#include <stdio.h>

int main() {
    int n,leap=0;
    scanf("%d",&n);
    if(n%4==0)
        leap=1;
    if(n>1918)
    if(leap)
        if(n%100==0 && n%400!=0)
            printf("13.09.%d",n);
        else
            printf("12.09.%d",n);
    else
        printf("13.09.%d",n);
    if(n<1918){
        if(leap==0)
            printf("13.09.%d",n);
        else
            printf("12.09.%d",n);
    }
    if(n==1918)
        printf("26.09.%d",n);

    return 0;
}
