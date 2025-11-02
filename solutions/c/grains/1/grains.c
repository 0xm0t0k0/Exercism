#include "grains.h"

#define TOTAL_SQUARES 64

uint64_t square(uint8_t index)
{
    if (index == 1)
        return 1;
    else 
        return square(index - 1) * 2;
        
}

uint64_t total(void)
{
    
    uint64_t sum = 0;
    for (int i = 1; i <= TOTAL_SQUARES; i++)
    {
        sum += square(i);
    }

    return sum;
}