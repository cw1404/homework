#include <stdio.h>

int main() {

    printf("請輸入一個整數︰");

    int i;

    scanf("%d", &i);

    i = i % 10;

    //line 12 is incomplete, refer to page 4 of Operation slides to achieve the requirement.
    printf("這個整數的個位數是%d\n", i);
}
