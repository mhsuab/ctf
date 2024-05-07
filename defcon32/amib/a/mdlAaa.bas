
Public Sub Proc_2_0_40E430
  loc_0040E473: If arg_C = 0 Then
  loc_0040E480:   GoTo loc_0040E59A
  loc_0040E485: End If
  loc_0040E489: If arg_C = 31 Then
  loc_0040E49A:   var_14 = -2147483648
  loc_0040E4A2:   GoTo loc_0040E59A
  loc_0040E4A7: End If
  loc_0040E4AA: If arg_C >= 0 Then
  loc_0040E4B0:   If arg_C <= 31 Then GoTo loc_0040E53C
  loc_0040E500: Err = CInt(6)
  loc_0040E53C: 
  loc_0040E550: idiv [esi+ebx*4]
  loc_0040E55C: If Me Then
  loc_0040E55E:   edi = arg_C - 1
  loc_0040E568:   idiv [esi+ecx*4]
  loc_0040E56E: End If
  loc_0040E573: GoTo loc_0040E59A
  loc_0040E599: Exit Sub
  loc_0040E59A: 'Referenced from: 0040E480
End Sub

Public Sub Proc_2_1_40E870
  loc_0040E8C2: 0.Release 'Ignore this = 0.Release 'Ignore this + 0 And 63
  loc_0040E8CA: esi = 0.Release 'Ignore this+0 And 63 + 1
  loc_0040E8E1: var_20 = Len(Me)
  loc_0040E8E4: var_1C = 0.Release 'Ignore this+0 And 63 + 1
  loc_0040E8E7: ReDim var_2C(0 To esi-00000001h)
  loc_0040E8F5: If edi < 0 Then
  loc_0040E901:   edi = edi + 0 And 3
  loc_0040E930:   var_54 = Mid(Me, 0.QueryInterface, edi+0 And 3)
  loc_0040E93E:   var_34 = CStr(var_54)
  loc_0040E94B:   var_78 = AscB(var_34)
  loc_0040E951:   edi+0 And 3 = edi+0 And 3 - eax+00000014h
  loc_0040E960:   If Not Sign(-2147483645 - 0) Then
  loc_0040E962:     edi = -2147483645 - 1
  loc_0040E966:     edi = -4 + 1
  loc_0040E967:   End If
  loc_0040E975:   var_eax = Proc_1_23_40E280(AscB(var_34) And 255, -4 + 1, 0.QueryInterface 'Ignore this)
  loc_0040E9A4:   GoTo loc_0040E8F0
  loc_0040E9A9: End If
  loc_0040E9AC: var_54 = var_54 + AscB(var_34) And 255 And 3
  loc_0040E9B7: If Not Sign(-2147483645 - 0) Then
  loc_0040E9B9:   edi = -2147483645 - 1
  loc_0040E9BD:   edi = -4 + 1
  loc_0040E9BE: End If
  loc_0040E9C1: var_54+AscB(var_34) And 255 And 3 = var_54+AscB(var_34) And 255 And 3 - ecx+00000014h
  loc_0040E9D3: var_84 = var_2C(4)(var_54+AscB(var_34) And 255 And 3*4)
  loc_0040E9D9: var_eax = Proc_1_23_40E280(128, -4 + 1, )
  loc_0040E9ED: var_eax = Proc_1_23_40E280(var_20, 3, )
  loc_0040E9FF: var_1C = var_1C - var_2C(6)
  loc_0040EA06: var_eax = Proc_2_0_40E430(var_20, 29, )
  loc_0040EA14: var_1C = var_1C - var_2C(6)
  loc_0040EA22: var_18 = var_2C
  loc_0040EA2D: GoTo loc_0040EA5E
  loc_0040EA33: If var_4 Then
  loc_0040EA41: End If
  loc_0040EA5D: Exit Sub
  loc_0040EA5E: 'Referenced from: 0040EA2D
End Sub

Public Sub Proc_2_2_40EA90
  loc_0040EAE5: 
  loc_0040EAEC: If esi <= 3 Then
  loc_0040EAFB:   call Proc_2_0_40E430(Me, esi*8, %x1 = %StkVar3 & %StkVar2)
  loc_0040EB09:   var_1C = False
  loc_0040EB17:   var_68 = var_1C
  loc_0040EB41:   var_88 = var_18
  loc_0040EB7D:   var_18 = var_18 & Right(&H402FCC & Hex(var_1C), 2)
  loc_0040EBA3:   esi = esi + 00000001h
  loc_0040EBA5:   GoTo loc_0040EAE5
  loc_0040EBAA: End If
  loc_0040EBAF: GoTo loc_0040EBDC
  loc_0040EBB5: If var_4 Then
  loc_0040EBC0: End If
  loc_0040EBDB: Exit Sub
  loc_0040EBDC: 'Referenced from: 0040EBAF
End Sub

Public Sub Proc_2_3_40EC00
  Dim var_34 As Me
  Dim var_30 As Me
  Dim var_2C As Me
  Dim var_28 As Me
  loc_0040EC62: var_eax = Proc_2_1_40E870(Me, edi, esi)
  loc_0040EC72: var_40 = Proc_2_1_40E870(Me, edi, esi)
  loc_0040EC9A: call UBound(00000001h, var_40, 0)
  loc_0040ECA0: var_84 = UBound(00000001h, var_40, 0)
  loc_0040ECAF: If esi <= UBound(00000001h, var_40, 0) Then
  loc_0040ECBE:   var_24 = var_30
  loc_0040ECCD:   esi = esi - edx+00000014h
  loc_0040ECD8:   var_3C = var_34
  loc_0040ECE0:   var_18 = var_2C
  loc_0040ECE7:   var_eax = Proc_40E6F0(var_28, var_2C, var_30)
  loc_0040ED15:   var_eax = Proc_40E6F0(var_34, var_28, var_2C)
  loc_0040ED43:   var_eax = Proc_40E6F0(var_30, var_34, var_28)
  loc_0040ED71:   var_eax = Proc_40E6F0(var_2C, var_30, var_34)
  loc_0040ED9F:   var_eax = Proc_40E6F0(var_28, var_2C, var_30)
  loc_0040EDCD:   var_eax = Proc_40E6F0(var_34, var_28, var_2C)
  loc_0040EDFB:   var_eax = Proc_40E6F0(var_30, var_34, var_28)
  loc_0040EE29:   var_eax = Proc_40E6F0(var_2C, var_30, var_34)
  loc_0040EE57:   var_eax = Proc_40E6F0(var_28, var_2C, var_30)
  loc_0040EE85:   var_eax = Proc_40E6F0(var_34, var_28, var_2C)
  loc_0040EEB3:   var_eax = Proc_40E6F0(var_30, var_34, var_28)
  loc_0040EEE1:   var_eax = Proc_40E6F0(var_2C, var_30, var_34)
  loc_0040EF0F:   var_eax = Proc_40E6F0(var_28, var_2C, var_30)
  loc_0040EF3D:   var_eax = Proc_40E6F0(var_34, var_28, var_2C)
  loc_0040EF6B:   var_eax = Proc_40E6F0(var_30, var_34, var_28)
  loc_0040EF99:   var_eax = Proc_40E6F0(var_2C, var_30, var_34)
  loc_0040EFC7:   var_eax = Proc_40E750(var_28, var_2C, var_30)
  loc_0040EFF5:   var_eax = Proc_40E750(var_34, var_28, var_2C)
  loc_0040F023:   var_eax = Proc_40E750(var_30, var_34, var_28)
  loc_0040F050:   var_eax = Proc_40E750(var_2C, var_30, var_34)
  loc_0040F07E:   var_eax = Proc_40E750(var_28, var_2C, var_30)
  loc_0040F0AC:   var_eax = Proc_40E750(var_34, var_28, var_2C)
  loc_0040F0DA:   var_eax = Proc_40E750(var_30, var_34, var_28)
  loc_0040F108:   var_eax = Proc_40E750(var_2C, var_30, var_34)
  loc_0040F136:   var_eax = Proc_40E750(var_28, var_2C, var_30)
  loc_0040F164:   var_eax = Proc_40E750(var_34, var_28, var_2C)
  loc_0040F192:   var_eax = Proc_40E750(var_30, var_34, var_28)
  loc_0040F1C0:   var_eax = Proc_40E750(var_2C, var_30, var_34)
  loc_0040F1EE:   var_eax = Proc_40E750(var_28, var_2C, var_30)
  loc_0040F21C:   var_eax = Proc_40E750(var_34, var_28, var_2C)
  loc_0040F24A:   var_eax = Proc_40E750(var_30, var_34, var_28)
  loc_0040F278:   var_eax = Proc_40E750(var_2C, var_30, var_34)
  loc_0040F2A6:   var_eax = Proc_40E7B0(var_28, var_2C, var_30)
  loc_0040F2D4:   var_eax = Proc_40E7B0(var_34, var_28, var_2C)
  loc_0040F302:   var_eax = Proc_40E7B0(var_30, var_34, var_28)
  loc_0040F330:   var_eax = Proc_40E7B0(var_2C, var_30, var_34)
  loc_0040F35E:   var_eax = Proc_40E7B0(var_28, var_2C, var_30)
  loc_0040F38C:   var_eax = Proc_40E7B0(var_34, var_28, var_2C)
  loc_0040F3BA:   var_eax = Proc_40E7B0(var_30, var_34, var_28)
  loc_0040F3E8:   var_eax = Proc_40E7B0(var_2C, var_30, var_34)
  loc_0040F416:   var_eax = Proc_40E7B0(var_28, var_2C, var_30)
  loc_0040F443:   var_eax = Proc_40E7B0(var_34, var_28, var_2C)
  loc_0040F471:   var_eax = Proc_40E7B0(var_30, var_34, var_28)
  loc_0040F49F:   var_eax = Proc_40E7B0(var_2C, var_30, var_34)
  loc_0040F4CD:   var_eax = Proc_40E7B0(var_28, var_2C, var_30)
  loc_0040F4FB:   var_eax = Proc_40E7B0(var_34, var_28, var_2C)
  loc_0040F529:   var_eax = Proc_40E7B0(var_30, var_34, var_28)
  loc_0040F557:   var_eax = Proc_40E7B0(var_2C, var_30, var_34)
  loc_0040F584:   var_eax = Proc_40E810(var_28, var_2C, var_30)
  loc_0040F5B2:   var_eax = Proc_40E810(var_34, var_28, var_2C)
  loc_0040F5E0:   var_eax = Proc_40E810(var_30, var_34, var_28)
  loc_0040F60E:   var_eax = Proc_40E810(var_2C, var_30, var_34)
  loc_0040F63C:   var_eax = Proc_40E810(var_28, var_2C, var_30)
  loc_0040F66A:   var_eax = Proc_40E810(var_34, var_28, var_2C)
  loc_0040F698:   var_eax = Proc_40E810(var_30, var_34, var_28)
  loc_0040F6C6:   var_eax = Proc_40E810(var_2C, var_30, var_34)
  loc_0040F6F4:   var_eax = Proc_40E810(var_28, var_2C, var_30)
  loc_0040F722:   var_eax = Proc_40E810(var_34, var_28, var_2C)
  loc_0040F750:   var_eax = Proc_40E810(var_30, var_34, var_28)
  loc_0040F77E:   var_eax = Proc_40E810(var_2C, var_30, var_34)
  loc_0040F7AC:   var_eax = Proc_40E810(var_28, var_2C, var_30)
  loc_0040F7DA:   var_eax = Proc_40E810(var_34, var_28, var_2C)
  loc_0040F808:   var_eax = Proc_40E810(var_30, var_34, var_28)
  loc_0040F836:   var_eax = Proc_40E810(var_2C, var_30, var_34)
  loc_0040F840:   var_eax = Proc_40E5F0(var_28, var_28, var_28)
  loc_0040F84D:   var_28 = Proc_40E5F0(var_28, var_28, var_28)
  loc_0040F850:   var_eax = Proc_40E5F0(var_2C, var_18, eax+edx*4+00000024h)
  loc_0040F858:   var_2C = Proc_40E5F0(var_2C, var_18, eax+edx*4+00000024h)
  loc_0040F860:   var_eax = Proc_40E5F0(var_30, var_24, global_EB86D391)
  loc_0040F868:   var_30 = Proc_40E5F0(var_30, var_24, global_EB86D391)
  loc_0040F870:   var_eax = Proc_40E5F0(var_34, var_3C, 15)
  loc_0040F87A:   var_34 = Proc_40E5F0(var_34, var_3C, 15)
  loc_0040F87D:   esi-edx+00000014h = esi-edx+00000014h + 00000010h
  loc_0040F87F:   GoTo loc_0040ECA9
  loc_0040F884: End If
  loc_0040F888: var_eax = Proc_2_2_40EA90(var_28, global_BD3AF235, eax+edx*4+00000034h)
  loc_0040F898: var_44 = Proc_2_2_40EA90(var_28, global_BD3AF235, eax+edx*4+00000034h)
  loc_0040F89F: var_eax = Proc_2_2_40EA90(var_2C, var_44, global_4E0811A1)
  loc_0040F8B9: var_4C = eax+edx*4+0000003Ch & Proc_2_2_40EA90(var_2C, var_44, global_4E0811A1)
  loc_0040F8C0: var_eax = Proc_2_2_40EA90(var_30, var_4C, global_FE2CE6E0)
  loc_0040F8D4: var_54 = eax+edx*4+00000004h & Proc_2_2_40EA90(var_30, var_4C, global_FE2CE6E0)
  loc_0040F8DB: var_eax = Proc_2_2_40EA90(var_34, var_54, global_85845DD1)
  loc_0040F8E5: var_58 = Proc_2_2_40EA90(var_34, var_54, global_85845DD1)
  loc_0040F8ED: var_60 = eax+edx*4+0000000Ch & var_58
  loc_0040F8FC: var_78 = LCase(eax+edx*4+0000000Ch & var_58)
  loc_0040F911: var_20 = var_78
  loc_0040F94B: GoTo loc_0040F990
  loc_0040F951: If var_4 Then
  loc_0040F95C: End If
  loc_0040F98F: Exit Sub
  loc_0040F990: 'Referenced from: 0040F94B
End Sub
