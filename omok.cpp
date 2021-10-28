#include <stdio.h>
#include <stdlib.h>

int judge( int t ; int la ; int po ; int a[la][po] )
{
    if ( t % 2 == 0 )
    {
        int win = 0 ;
        int fo = 4 ;
        int ca =  0;
        switch(ca)
        {
        case 0:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la+i][po] == 1) win++;
                else if( a[la+(i-fo)][po] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 1:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la][po+i] == 1) win++;
                else if( a[la][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 2:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la+i][po+i] == 1) win++;
                else if( a[la+(i-fo)][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 3:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la-i][po+i] == 1) win++;
                else if( a[la+(fo-i)][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        }

    }
    if ( t % 2 == 1 )
    {
        int win = 0 ;
        int fo = 4 ;
        int ca =  0;
        switch(ca)
        {
        case 0:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la+i][po] == 1) win++;
                else if( a[la+(i-fo)][po] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 1:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la][po+i] == 1) win++;
                else if( a[la][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 2:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la+i][po+i] == 1) win++;
                else if( a[la+(i-fo)][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        case 3:
            for( int i = 1 ; i <= fo ; i ++ )
            {
                if( a[la-i][po+i] == 1) win++;
                else if( a[la+(fo-i)][po+(i-fo)] == 1) win++;
                if( win == 4 ) return win;
                else return ca++;
            }
        }

    }
    return 5;
}

int main()
{
    int a[19][19]={0};
    int t = 0;
    int la,po = 0;
    printf("시작\n");
    printf("흑돌 = 1 흰돌 = 2\n");

    while(1)
    {
        if( t % 2 == 0 )
        {
        printf("black turn\n");
        scanf("%d %d",&la,&po);
        if( la>=19 || po>=19 )continue;
        if( a[la][po] != 0 )continue;
        a[la][po] = 1;
        int judge(t,la,po,a[la][po]) = d;
        if ( d == 5 ) printf("win");
        t++ ;
        for( int i = 0 ; i < 19 ; i++ )
            {
            for( int j = 0 ; j < 19 ; j++ )
                {
                if(a[i][j]==0) printf("  ");
                else printf("%d ",a[i][j]);
                }
            printf("\n");
            }
        }

        if( t % 2 == 1 )
        {
        printf("white turn\n");
        scanf("%d %d",&la,&po);
        if( la>=19 || po>=19 )continue;
        if( a[la][po] != 0 )continue;
        a[la][po] = 2;
        t++ ;
        for( int i = 0 ; i < 19 ; i++ )
            {
            for( int j = 0 ; j < 19 ; j++ )
                {
                if(a[i][j]==0) printf("  ");
                else printf("%d ",a[i][j]);
                }
            printf("\n");
            }
        }
    }
    return 0 ;
}

