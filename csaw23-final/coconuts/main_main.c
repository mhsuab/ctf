// main.main
void __fastcall main_main()
{
  __int64 v0; // rax
  __int64 v1; // rbx
  int v2; // r9d
  int v3; // r10d
  int v4; // r11d
  __int64 v5; // r14
  __int64 v6; // rsi
  __int64 v7; // rdx
  int v8; // r8d
  int v9; // r9d
  int v10; // r10d
  int v11; // r11d
  __int64 argv_0_Sir_Lancelot_of_Camelot; // rax
  int v13; // ecx
  int v14; // ecx
  int v15; // r8d
  int v16; // r9d
  int v17; // r10d
  int v18; // r11d
  int v19; // ecx
  int v20; // r8d
  int v21; // r9d
  int v22; // r10d
  int v23; // r11d
  int v24; // ecx
  int v25; // r8d
  int v26; // r9d
  int v27; // r10d
  int v28; // r11d
  __int64 str_lancelot_unk_prob_full_path_filename; // rax
  __int64 v30; // rcx
  int v31; // r8d
  int v32; // r9d
  int v33; // r10d
  int v34; // r11d
  __int64 v35; // rcx
  int v36; // r8d
  int v37; // r9d
  int v38; // r10d
  int v39; // r11d
  __int64 str_king_authur_unk_2023tag11tag10; // rax
  int v41; // edi
  const char *v42; // rsi
  int v43; // r8d
  int v44; // r9d
  int v45; // r10d
  int v46; // r11d
  int v47; // ebx
  int v48; // eax
  int v49; // r10d
  int v50; // r11d
  __int64 v51; // rax
  __int64 v52; // rcx
  int v53; // r8d
  int v54; // r9d
  int v55; // r10d
  int v56; // r11d
  _QWORD *v57; // rax
  __int64 v58; // [rsp+0h] [rbp-E8h]
  __int64 v59; // [rsp+0h] [rbp-E8h]
  __int64 v60; // [rsp+0h] [rbp-E8h]
  __int64 v61; // [rsp+0h] [rbp-E8h]
  __int64 v62; // [rsp+0h] [rbp-E8h]
  __int64 v63; // [rsp+0h] [rbp-E8h]
  __int64 v64; // [rsp+0h] [rbp-E8h]
  __int64 v65; // [rsp+0h] [rbp-E8h]
  __int64 v66; // [rsp+8h] [rbp-E0h]
  __int64 v67; // [rsp+8h] [rbp-E0h]
  __int64 v68; // [rsp+10h] [rbp-D8h]
  __int64 v69; // [rsp+10h] [rbp-D8h]
  __int64 v70; // [rsp+18h] [rbp-D0h]
  __int64 v71; // [rsp+18h] [rbp-D0h]
  __int64 v72; // [rsp+68h] [rbp-80h]
  char str_thgink_neerg[12]; // [rsp+74h] [rbp-74h] BYREF
  char v74[32]; // [rsp+80h] [rbp-68h] BYREF
  const char *str_frecnch_tauter_unk; // [rsp+A0h] [rbp-48h]
  __int64 str_rabbit_unk; // [rsp+A8h] [rbp-40h]
  const char *str_tim_the_enchanter_dot_dot_dot; // [rsp+B0h] [rbp-38h]
  __int64 str_sir_robin; // [rsp+B8h] [rbp-30h]
  __int64 str_galahad; // [rsp+C0h] [rbp-28h]
  __int64 str_green_knight; // [rsp+C8h] [rbp-20h]
  __int64 v81; // [rsp+D0h] [rbp-18h]
  __int128 v82; // [rsp+D8h] [rbp-10h] BYREF

  while ( (unsigned __int64)v74 <= *(_QWORD *)(v5 + 16) )
    v0 = runtime_morestack_noctxt(v0);
  if ( !qword_7FF6120E5378 )
    runtime_panicSliceB(1LL, v1);
  if ( qword_7FF6120E5378 == 1 )
  {
    v7 = 0LL;
    v6 = 0LL;
  }
  else
  {
    if ( (unsigned __int64)qword_7FF6120E5378 <= 1 )
      runtime_panicIndex(1LL, v1);
    v6 = *(_QWORD *)(qword_7FF6120E5370 + 16);
    v7 = *(_QWORD *)(qword_7FF6120E5370 + 24);
  }
  v72 = v7;
  v81 = v6;
  *(_QWORD *)&v82 = &RTYPE_string;
  *((_QWORD *)&v82 + 1) = &ptr_never_get_argument_with_knight;
  fmt_Println(
    (unsigned int)&v82,
    1,
    1,
    (unsigned int)&RTYPE_string,
    v6,
    (unsigned int)&ptr_never_get_argument_with_knight,
    v2,
    v3,
    v4);
  if ( v72 == 23
    && (argv_0_Sir_Lancelot_of_Camelot = runtime_memequal(v81, (__int64)"Sir Lancelot of Camelot"),
        (_BYTE)argv_0_Sir_Lancelot_of_Camelot) )
  {
    main__Cfunc_green_knight(                   // C function call has anti debugging
      argv_0_Sir_Lancelot_of_Camelot,
      (unsigned int)"Sir Lancelot of Camelot",
      v13,
      (int)&RTYPE_string,
      v6,
      v8,
      v9,
      v10,
      v11,
      v58);
    str_green_knight = main__Cfunc_GoString(v59);
    main__Cfunc_rabbit_of_caerbannog(
      str_green_knight,
      (unsigned int)"Sir Lancelot of Camelot",
      v14,
      (int)&RTYPE_string,
      v6,
      v15,
      v16,
      v17,
      v18,
      v59);
    str_rabbit_unk = main__Cfunc_GoString(v60);
    main__Cfunc_sir_galahad(
      str_rabbit_unk,
      (unsigned int)"Sir Lancelot of Camelot",
      v19,
      (int)&RTYPE_string,
      v6,
      v20,
      v21,
      v22,
      v23,
      v60);
    str_galahad = main__Cfunc_GoString(v61);
    main__Cfunc_sir_lancelot(
      str_galahad,
      (unsigned int)"Sir Lancelot of Camelot",
      v24,
      (int)&RTYPE_string,
      v6,
      v25,
      v26,
      v27,
      v28,
      v61);
    str_lancelot_unk_prob_full_path_filename = main__Cfunc_GoString(v62);
    str_tim_the_enchanter_dot_dot_dot = main_tim_the_enchanter(
                                          str_lancelot_unk_prob_full_path_filename,
                                          (int)"Sir Lancelot of Camelot",
                                          str_galahad,
                                          (unsigned __int64)"Sir Lancelot of Camelot");
    main__Cfunc_sir_robin(
      (__int64)str_tim_the_enchanter_dot_dot_dot,
      (__int64)"Sir Lancelot of Camelot",
      v30,
      (int)"Sir Lancelot of Camelot",
      v6,
      v31,
      v32,
      v33,
      v34,
      v62);
    str_sir_robin = main__Cfunc_GoString(v63);
    main__Cfunc_king_arthur(
      str_sir_robin,
      (__int64)"Sir Lancelot of Camelot",
      v35,
      (int)"Sir Lancelot of Camelot",
      v6,
      v36,
      v37,
      v38,
      v39,
      v63);
    str_king_authur_unk_2023tag11tag10 = main__Cfunc_GoString(v64);
    str_frecnch_tauter_unk = main_french_taunter(// return '<space>are to be broken.'
                               str_king_authur_unk_2023tag11tag10,
                               (int)"Sir Lancelot of Camelot",
                               str_sir_robin,
                               (unsigned __int64)"Sir Lancelot of Camelot");
    qmemcpy(str_thgink_neerg, "thgink_neerg", sizeof(str_thgink_neerg));
    v41 = str_green_knight;
    v42 = "Sir Lancelot of Camelot";
    if ( (unsigned __int8)main_bors(
                            (__int64)str_thgink_neerg,
                            0xCLL,
                            0xC,
                            str_green_knight,
                            (unsigned __int64)"Sir Lancelot of Camelot") )
    {
      v47 = (int)str_tim_the_enchanter_dot_dot_dot;
      v48 = runtime_concatstring3(
              (unsigned int)v74,
              (_DWORD)str_tim_the_enchanter_dot_dot_dot,
              (unsigned int)"Sir Lancelot of Camelot",
              str_rabbit_unk,
              (unsigned int)"Sir Lancelot of Camelot",
              (_DWORD)str_frecnch_tauter_unk,
              (unsigned int)"Sir Lancelot of Camelot",
              v45,
              v46,
              v64,
              v66,
              v68,
              v70);
      v82 = 0LL;
      v41 = v48;
      LODWORD(v42) = v47;
      v51 = runtime_concatstring3(
              0,
              (unsigned int)"csawctf{",
              8,
              v48,
              v47,
              (unsigned int)"}",
              1,
              v49,
              v50,
              v65,
              v67,
              v69,
              v71);
      v57 = runtime_convTstring(v51, (__int64)"csawctf{", v52, v41, v47, v53, v54, v55, v56);
      *(_QWORD *)&v82 = &RTYPE_string;
      *((_QWORD *)&v82 + 1) = v57;
    }
    else
    {
      *(_QWORD *)&v82 = &RTYPE_string;
      *((_QWORD *)&v82 + 1) = &ptr_are_you_suggesting_coconuts_migrate;
    }
    fmt_Println((unsigned int)&v82, 1, 1, v41, (_DWORD)v42, v43, v44, v45, v46);
  }
  else
  {
    *(_QWORD *)&v82 = &RTYPE_string;
    *((_QWORD *)&v82 + 1) = &ptr_auuuuuuugh;
    fmt_Println((unsigned int)&v82, 1, 1, (unsigned int)&RTYPE_string, v6, v8, v9, v10, v11);
  }
}