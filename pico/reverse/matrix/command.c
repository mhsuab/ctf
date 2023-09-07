__int64 __fastcall sub_555555555350(struct_a1 *a1, unsigned __int16 a2[2])
{
  char *ptr_bytes; // rdi
  __int64 idx_low; // rax MAPDST
  unsigned __int16 nxt_idx; // cx
  char _input; // al
  _WORD *v8; // rax
  _WORD *v9; // rdi
  __int64 result; // rax
  __int16 v11; // dx
  __int16 v12; // cx
  _WORD *v13; // rax
  _WORD *v14; // rax
  bool v15; // sf
  __int16 v16; // cx
  _WORD *stack; // rdx
  _WORD *v18; // rcx
  _WORD *v19; // rax
  __int16 v20; // dx
  _WORD *v21; // rax
  __int16 v22; // dx
  _WORD *v23; // rdx
  _WORD *mem; // rax
  _WORD *v25; // rax
  __int16 v26; // dx
  _WORD *v27; // rdx
  _WORD *v28; // rax
  _WORD *v29; // rdx
  __int16 v30; // ax
  _WORD *v31; // rax
  bool v32; // zf
  _WORD *v33; // rax
  _WORD *v34; // rax
  bool v35; // cc
  _WORD *v36; // rax
  __int16 v37; // dx
  unsigned __int8 input_char; // al
  _WORD *v39; // rdx

  ptr_bytes = a1->ptr_bytes;
  idx_low = LOWORD(a1->idx);
  nxt_idx = idx_low + 1;
  LOWORD(a1->idx) = idx_low + 1;
  _input = ptr_bytes[idx_low];
  switch ( _input )
  {
    case 0:
      return 1LL;
    case 1:
      result = 0LL;
      if ( a2 )
      {
        stack = a1->stack;
        *(_BYTE *)a2 = 0;
        v18 = stack - 1;
        LOWORD(stack) = *(stack - 1);
        a1->stack = v18;
        a2[1] = (unsigned __int16)stack;
      }
      return result;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 0xA:
    case 0xB:
    case 0xC:
    case 0xD:
    case 0xE:
    case 0xF:
    case 0x15:
    case 0x16:
    case 0x17:
    case 0x18:
    case 0x19:
    case 0x1A:
    case 0x1B:
    case 0x1C:
    case 0x1D:
    case 0x1E:
    case 0x1F:
    case 0x22:
    case 0x23:
    case 0x24:
    case 0x25:
    case 0x26:
    case 0x27:
    case 0x28:
    case 0x29:
    case 0x2A:
    case 0x2B:
    case 0x2C:
    case 0x2D:
    case 0x2E:
    case 0x2F:
      goto ret_0_and_set_a2_to_1;
    case 0x10:
      v25 = a1->stack;
      v26 = *(v25 - 1);
      a1->stack = v25 + 1;
      *v25 = v26;
      return 1LL;
    case 0x11:
      --a1->stack;
      return 1LL;
    case 0x12:
      v36 = a1->stack;
      v37 = *(v36 - 2) + *(v36 - 1);
      a1->stack = v36 - 1;
      *(v36 - 2) = v37;
      return 1LL;
    case 0x13:
      v19 = a1->stack;
      v20 = *(v19 - 2) - *(v19 - 1);
      a1->stack = v19 - 1;
      *(v19 - 2) = v20;
      return 1LL;
    case 0x14:
      v21 = a1->stack;
      v22 = *(v21 - 2);
      *(v21 - 2) = *(v21 - 1);
      a1->stack = v21;
      *(v21 - 1) = v22;
      return 1LL;
    case 0x20:
      v23 = a1->stack - 1;
      a1->stack = v23;
      LOWORD(v23) = *v23;
      mem = a1->mem;
      a1->mem = mem + 1;
      *mem = (_WORD)v23;
      return 1LL;
    case 0x21:
      v27 = a1->mem - 1;
      a1->mem = v27;
      LOWORD(v27) = *v27;
      v28 = a1->stack;
      a1->stack = v28 + 1;
      *v28 = (_WORD)v27;
      return 1LL;
    case 0x30:
      v29 = a1->stack - 1;
      v30 = *v29;
      a1->stack = v29;
      LOWORD(a1->idx) = v30;
      return 1LL;
    case 0x31:
      v31 = a1->stack;
      v32 = *(v31 - 2) == 0;
      v16 = *(v31 - 1);
      a1->stack = v31 - 2;
      if ( v32 )
        goto set_idx_and_ret_1;
      return 1LL;
    case 0x32:
      v33 = a1->stack;
      v32 = *(v33 - 2) == 0;
      v16 = *(v33 - 1);
      a1->stack = v33 - 2;
      if ( !v32 )
        goto set_idx_and_ret_1;
      return 1LL;
    case 0x33:
      v14 = a1->stack;
      v15 = (__int16)*(v14 - 2) < 0;
      v16 = *(v14 - 1);
      a1->stack = v14 - 2;
      if ( !v15 )
        return 1LL;
      goto set_idx_and_ret_1;
    case 0x34:
      v34 = a1->stack;
      v35 = *(v34 - 2) <= 0;
      v16 = *(v34 - 1);
      a1->stack = v34 - 2;
      if ( !v35 )
        return 1LL;
set_idx_and_ret_1:
      LOWORD(a1->idx) = v16;
      return 1LL;
    default:
      if ( _input == (char)0xC0 )
      {
        input_char = ((__int64 (__fastcall *)(char *, unsigned __int16 *__attribute__((__org_arrdim(0,2))), __int64))a1->getc)(
                       ptr_bytes,
                       a2,
                       idx_low);
        v39 = a1->stack;
        a1->stack = v39 + 1;
        *v39 = input_char;
        return 1LL;
      }
      if ( (unsigned __int8)_input > 0xC0u )
      {
        if ( _input == (char)0xC1 )
        {
          v8 = a1->stack;
          v9 = (_WORD *)*((unsigned __int8 *)v8 - 2);
          a1->stack = v8 - 1;
          a1->putc((__int64)v9, (__int64)a2);
          return 1LL;
        }
        goto ret_0_and_set_a2_to_1;
      }
      if ( _input == (char)0x80 )
      {
        v11 = idx_low + 2;
        v12 = ptr_bytes[nxt_idx];
        goto LABEL_10;
      }
      if ( _input == (char)0x81 )
      {
        v11 = idx_low + 3;
        v12 = *(_WORD *)&ptr_bytes[nxt_idx];
LABEL_10:
        v13 = a1->stack;
        LOWORD(a1->idx) = v11;
        a1->stack = v13 + 1;
        *v13 = v12;
        return 1LL;
      }
ret_0_and_set_a2_to_1:
      result = 0LL;
      if ( a2 )
        *(_BYTE *)a2 = 1;
      return result;
  }
}