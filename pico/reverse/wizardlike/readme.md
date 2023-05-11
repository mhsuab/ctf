# Wizardlike
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/318/)

## Description
> Do you seek your destiny in these deplorable dungeons? If so, you may want to look elsewhere. Many have gone before you and honestly, they've cleared out the place of all monsters, ne'erdowells, bandits and every other sort of evil foe. The dungeons themselves have seen better days too. There's a lot of missing floors and key passages blocked off. You'd have to be a real wizard to make any progress in this sorry excuse for a dungeon!  
> Download the game.  
> 'w', 'a', 's', 'd' moves your character and 'Q' quits. You'll need to improvise some wizardly abilities to find the flag in this dungeon crawl. '.' is floor, '#' are walls, '<' are stairs up to previous level, and '>' are stairs down to next level.

## What It Does
Game with multiple levels of mazes that use 'w,a,s,d' to move around.

## Solution
1. Run the program to test
    - more information of the maze will show up when moving around
    - **No way** to get to the next level from `level 4`
2. Use `IDA Pro` to disassemble the binary
    ```c
    __int64 __fastcall sub_402467(__int64 a1, char a2)
    {
        ...
        while ( game )
        {
            if ( display_stage_num_532F78 != stage_num_532F7C )
            {
                switch ( stage_num_532F7C )
                {
                    case 1:
                        init_display_401E35();
                        sub_401E9D(asc_51A840);
                        dword_532F70 = 2;
                        dword_532F74 = 1;
                        dword_535790 = 0;
                        dword_535794 = 0;
                        display_stage_num_532F78 = 1;
                    break;
                    ...
                }
            }
            ...
            for ( k = 0; k < v14; ++k )
            {
                for ( m = 0; m < v15; ++m )
                {
                    if ( dword_535790 + m > 99 || dword_535794 + k > 99 || dword_535790 + m < 0 || dword_535794 + k < 0 )
                    {
                        sub_406380(k, m, (unsigned int)&off_4DE004, m, v4, v5, v7);
                    }
                    else if ( (unsigned __int8)sub_401F3E(
                                                (unsigned int)dword_532F70,
                                                (unsigned int)dword_532F74,
                                                (unsigned int)(m + dword_535790),
                                                (unsigned int)(dword_535794 + k))
                        || display_array_536D80[100 * dword_535794 + 100 * k + dword_535790 + m] )
                    {
                        display_array_536D80[100 * dword_535794 + 100 * k + dword_535790 + m] = 1;
                        v17 = 0;
                        LOBYTE(v17) = byte_5394A0[100 * dword_535794 + 100 * k + dword_535790 + m];
                        sub_406380(k, m, (unsigned int)&v17, m, v4, v5, v7);
                    }
                }
            }
            ...
        }
    }
    ```
    - `init_display_401E35` set all the elements in `display_array_536D80` to **zero** and the elements of `display_array_536D80` will become **one** when moving around
    - Therefore, modify one byte in `game` of `init_display_401E35` s.t. the game display every information
        ```diff
        _BYTE *init_display_401E35()
        {
            _BYTE *result; // rax
            int i; // [rsp+0h] [rbp-8h]
            int j; // [rsp+4h] [rbp-4h]

            for ( i = 0; i <= 99; ++i )
            {
                for ( j = 0; j <= 99; ++j )
                {
                    result = &display_array_536D80[100 * i + j];
        -           *result = 0;
        +           *result = 1;
                }
            }
            return result;
        }
        ```

3. Run the modified version of `game`, [game_mod](./game_mod)
    ```
    #########
    #.@.....#  ......#...................................
    #.......#  ....................####.#####.#####..###.
    #........  .####.#..###..###..#.......#...#......#...
    #.......#  .#  #.#.#....#   #.#.......#...###...#....
    #.......#  .####.#.#....#   #.#.......#...#......#...
    #.......#  .#....#..###..###...####...#...#......###.
    #.......#  .#........................................
    #.......#  ..........................................
    #.......#
    #.......#
    #.......#
    #.......#
    #.......#
    #......>#
    #########
    ```
    - partial flag can be found in **ASCII Art** on the maze

4. Write [script](./solve.py) to print out every maze in the binary and combine every characters in **ASCII Art** to get the **flag**