#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <stdbool.h>

int isNumeric(const char *s);

/* 10000000 lines about 710MB */
int main(int argc, char *argv[])
{
	int r, a, b, fs;
	FILE *fp;

	if (argc < 3)
	{
		printf("Usage: %s file_name file_size\n", argv[0]);
		exit(0);
	}

    //if (!isNumeric(argv[2]))
    if (isNumeric(argv[2]) == false)
    {
        printf("Please input integer for file_size\n");
        exit(0);
    }

    fp = fopen(argv[1], "w+");
    fs = atoi(argv[2]);
    srand((unsigned)time(NULL));

    for (a=0; a<fs; a++)
    {
	fprintf(fp, "%d\t", a);

	for(b=0; b<7; b++)
	{
	    r=rand();
	    fprintf(fp, "%d\t", r);
	}
	fputs("\n", fp);
	}
    fclose(fp);

    return 0;
}

int isNumeric(const char *s)
{
    bool num_b;
    if (s == NULL || *s == '\0' || isspace(*s))
      return 0;

    char *p;
    strtod (s, &p);
    num_b = (*p == '\0');

    return num_b;
}
