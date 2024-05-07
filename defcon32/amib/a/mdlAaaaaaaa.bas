
Public Sub Proc_1_0_40A610
  Dim var_18 As Me
  loc_0040A654: If arg_C = 0 Then
  loc_0040A663:   GoTo loc_0040A7A6
  loc_0040A668: End If
  loc_0040A66B: If Me = 31 Then
  loc_0040A682:   var_14 = -2147483648
  loc_0040A685:   GoTo loc_0040A7A6
  loc_0040A68A: End If
  loc_0040A68F: If -2147483648 <= 31 Then ecx = 1
  loc_0040A696: If -2147483648 >= 0 Then edx = 1
  loc_0040A69B: If edx = 0 Then
  loc_0040A6EB:   var_18 = CInt(6)
  loc_0040A727: End If
  loc_0040A739: 0000001Fh = 0000001Fh - arg_C
  loc_0040A741: If [eax+esi] Then
  loc_0040A74E:   0000001Eh = 0000001Eh - arg_C
  loc_0040A75E:   var_14 = -2147483648
  loc_0040A766:   GoTo loc_0040A7A6
  loc_0040A768: End If
  loc_0040A77F: GoTo loc_0040A7A6
  loc_0040A7A5: Exit Sub
  loc_0040A7A6: 'Referenced from: 0040A663
End Sub

Public Sub Proc_1_1_40A7C0
  Dim var_28 As Me
  loc_0040A80A: If arg_10 = 0 Then
  loc_0040A821:   var_24 = arg_C
  loc_0040A82C:   GoTo loc_0040A9AD
  loc_0040A831: End If
  loc_0040A834: If var_24 = 31 Then
  loc_0040A83F:   If [edx] Then
  loc_0040A848: 
  loc_0040A855:     var_24 = CInt(1)
  loc_0040A860:     GoTo loc_0040A9AD
  loc_0040A865:   End If
  loc_0040A868:   GoTo loc_0040A848
  loc_0040A86A: End If
  loc_0040A87B: If edx = 0 Then
  loc_0040A8CB:   var_28 = CInt(6)
  loc_0040A907: End If
  loc_0040A91A: idiv [edi+ecx*4]
  loc_0040A93B: If [esi] Then
  loc_0040A94B:   idiv [esi+ecx*4-00000004h]
  loc_0040A965:   call Or(var_38, var_78, arg_C And 2147483646, var_38, var_48, var_58, var_68, var_28, Err, global_0040A9AE, global_0040A9AE, %ecx = %S_edx_S, 00411094h, arg_10)
  loc_0040A970:   var_24 = Or(var_38, var_78, var_24, var_38, var_48, var_58, var_68, var_28, Err, global_0040A9AE, global_0040A9AE, var_24 = %S_edx_S, 00411094h, arg_10)
  loc_0040A972: End If
  loc_0040A977: GoTo loc_0040A9AD
  loc_0040A97D: If var_4 Then
  loc_0040A988: End If
  loc_0040A9AC: Exit Sub
  loc_0040A9AD: 'Referenced from: 0040A82C
End Sub

Public Sub Proc_1_2_40A9E0
  Dim var_28 As Me
  loc_0040AA2A: If arg_10 = 0 Then
  loc_0040AA31:   var_70 = arg_C
  loc_0040AA34:   GoTo loc_0040AB25
  loc_0040AA39: End If
  loc_0040AA3C: If arg_C = 7 Then
  loc_0040AA44:   If [edx] Then
  loc_0040AA54:     GoTo loc_0040AB2C
  loc_0040AA59:   End If
  loc_0040AA63:   GoTo loc_0040AB2C
  loc_0040AA68: End If
  loc_0040AA6D: If arg_C <= 7 Then ecx = 1
  loc_0040AA74: If arg_C >= 0 Then edx = 1
  loc_0040AA79: If edx = 0 Then
  loc_0040AAC9:   var_28 = CInt(6)
  loc_0040AB05: End If
  loc_0040AB0D: 004110B0h = 004110B0h - arg_10
  loc_0040AB1F: [ecx+edx] = [ecx+edx] * 
  loc_0040AB25: 'Referenced from: 0040AA34
  loc_0040AB2C: 'Referenced from: 0040AA54
  loc_0040AB32: var_24 = arg_C
  loc_0040AB3D: GoTo loc_0040AB73
  loc_0040AB43: If var_4 Then
  loc_0040AB4E: End If
  loc_0040AB72: Exit Sub
  loc_0040AB73: 'Referenced from: 0040AB3D
End Sub

Public Sub Proc_1_3_40ABB0
  Dim var_28 As Me
  loc_0040ABFA: If arg_10 = 0 Then
  loc_0040AC01:   var_70 = arg_C
  loc_0040AC04:   GoTo loc_0040ACEA
  loc_0040AC09: End If
  loc_0040AC0C: If arg_C = 7 Then
  loc_0040AC14:   If [edx] Then
  loc_0040AC24:     GoTo loc_0040ACF1
  loc_0040AC29:   End If
  loc_0040AC33:   GoTo loc_0040ACF1
  loc_0040AC38: End If
  loc_0040AC3D: If arg_C <= 7 Then ecx = 1
  loc_0040AC44: If arg_C >= 0 Then edx = 1
  loc_0040AC49: If edx = 0 Then
  loc_0040AC99:   var_28 = CInt(6)
  loc_0040ACD5: End If
  loc_0040ACE4: div [edx+ecx]
  loc_0040ACEA: 'Referenced from: 0040AC04
  loc_0040ACF1: 'Referenced from: 0040AC24
  loc_0040ACF7: var_24 = arg_C
  loc_0040AD02: GoTo loc_0040AD38
  loc_0040AD08: If var_4 Then
  loc_0040AD13: End If
  loc_0040AD37: Exit Sub
  loc_0040AD38: 'Referenced from: 0040AD02
End Sub

Public Sub Proc_1_4_40AD70
  loc_0040ADB2: var_eax = Proc_1_0_40A610(arg_C, arg_10, arg_C)
  loc_0040ADB9: var_4C = Proc_1_0_40A610(arg_C, arg_10, arg_C)
  loc_0040ADC1: 00000020h = 00000020h - arg_10
  loc_0040ADD6: var_eax = Proc_1_1_40A7C0(var_34, arg_C, &H20)
  loc_0040ADE7: call Or(var_44, var_34, var_54, arg_10, ebx)
  loc_0040ADF2: var_24 = Or(var_44, var_34, var_54, arg_10, ebx)
  loc_0040AE06: GoTo loc_0040AE2B
  loc_0040AE0C: If var_4 Then
  loc_0040AE17: End If
  loc_0040AE2A: Exit Sub
  loc_0040AE2B: 'Referenced from: 0040AE06
End Sub

Public Sub Proc_1_5_40AE60
  loc_0040AEA6: var_eax = Proc_1_2_40A9E0(var_34, arg_C, arg_10)
  loc_0040AEB6: 00000008h = 00000008h - arg_10
  loc_0040AEC0: var_eax = Proc_1_3_40ABB0(var_44, arg_C, 8)
  loc_0040AED1: call Or(var_54, var_44, var_34, arg_C, arg_10, ebx)
  loc_0040AEDC: var_24 = Or(var_54, var_44, var_34, arg_C, arg_10, ebx)
  loc_0040AEFA: GoTo loc_0040AF23
  loc_0040AF00: If var_4 Then
  loc_0040AF0B: End If
  loc_0040AF22: Exit Sub
  loc_0040AF23: 'Referenced from: 0040AEFA
End Sub

Public Sub Proc_1_6_40AF60
  loc_0040AFA2: 
  loc_0040AFA9: If esi <= 3 Then
  loc_0040AFC5:   var_50 = esi*8
  loc_0040AFC8:   var_28 = ecx+esi
  loc_0040AFCF:   var_eax = Proc_1_0_40A610(var_28, var_50, esi)
  loc_0040AFD4:   var_44 = Proc_1_0_40A610(var_28, var_50, esi)
  loc_0040AFEA:   call Or(var_3C, var_4C, var_24, arg_C)
  loc_0040AFF5:   var_24 = Or(var_3C, var_4C, var_24, arg_C)
  loc_0040AFFB:   esi = esi + 00000001h
  loc_0040AFFD:   GoTo loc_0040AFA2
  loc_0040AFFF: End If
  loc_0040B004: GoTo loc_0040B01F
  loc_0040B00A: If var_4 Then
  loc_0040B015: End If
  loc_0040B01E: Exit Sub
  loc_0040B01F: 'Referenced from: 0040B004
End Sub

Public Sub Proc_1_7_40B050
  loc_0040B09B: If 00000003h >= "" Then
  loc_0040B0AC:   edi.GetTypeInfoCount 'Ignore this = edi.GetTypeInfoCount 'Ignore this + arg_10
  loc_0040B0BE:   var_50 = esi*8
  loc_0040B0C1:   var_18 = ecx+esi
  loc_0040B0C8:   var_eax = Proc_1_0_40A610(var_18, var_50, arg_10)
  loc_0040B0CD:   var_44 = Proc_1_0_40A610(var_18, var_50, arg_10)
  loc_0040B0E3:   call Or(var_3C, var_4C, var_2C)
  loc_0040B0EE:   var_2C = Or(var_3C, var_4C, var_2C)
  loc_0040B0F4:   00000003h = 00000003h + True
  loc_0040B0F6:   GoTo loc_0040B098
  loc_0040B0F8: End If
  loc_0040B0FD: GoTo loc_0040B118
  loc_0040B103: If var_4 Then
  loc_0040B10E: End If
  loc_0040B117: Exit Sub
  loc_0040B118: 'Referenced from: 0040B0FD
End Sub

Public Sub Proc_1_8_40B150
  loc_0040B19B: If 00000003h >= "" Then
  loc_0040B1AC:   edi.GetTypeInfoCount 'Ignore this = edi.GetTypeInfoCount 'Ignore this + arg_10
  loc_0040B1BB:   00000003h = 00000003h - 00000003h
  loc_0040B1C4:   var_18 = ecx+esi
  loc_0040B1CB:   var_eax = Proc_1_0_40A610(var_18, var_50, arg_10)
  loc_0040B1D0:   var_44 = Proc_1_0_40A610(var_18, var_50, arg_10)
  loc_0040B1E6:   call Or(var_3C, var_4C, var_2C)
  loc_0040B1F1:   var_2C = Or(var_3C, var_4C, var_2C)
  loc_0040B1F7:   00000003h = 00000003h + True
  loc_0040B1F9:   GoTo loc_0040B198
  loc_0040B1FB: End If
  loc_0040B200: GoTo loc_0040B21B
  loc_0040B206: If var_4 Then
  loc_0040B211: End If
  loc_0040B21A: Exit Sub
  loc_0040B21B: 'Referenced from: 0040B200
End Sub

Public Sub Proc_1_9_40B250
  loc_0040B2B6: var_eax = Proc_1_1_40A7C0(var_20, Me, 8)
  loc_0040B2CD: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B2E3: var_ret_2 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B30F: var_eax = Proc_1_1_40A7C0(var_20, Me, 16)
  loc_0040B322: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B329: var_4C = arg_C
  loc_0040B33F: var_ret_4 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B366: var_eax = Proc_1_1_40A7C0(var_20, Me, &H18)
  loc_0040B37D: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B393: var_ret_6 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B3AC: GoTo loc_0040B3C2
  loc_0040B3C1: Exit Sub
  loc_0040B3C2: 'Referenced from: 0040B3AC
End Sub

Public Sub Proc_1_10_40B3E0
  loc_0040B44C: var_eax = Proc_1_1_40A7C0(var_20, Me, 8)
  loc_0040B45E: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B465: var_4C = arg_C
  loc_0040B47B: var_ret_2 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B4A9: var_eax = Proc_1_1_40A7C0(var_20, Me, 16)
  loc_0040B4BC: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B4C3: var_4C = arg_C
  loc_0040B4D9: var_ret_4 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B507: var_eax = Proc_1_1_40A7C0(var_20, Me, &H18)
  loc_0040B51E: var_38 = edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040B534: var_ret_6 = CByte(var_20 And edi.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040B556: GoTo loc_0040B56C
  loc_0040B56B: Exit Sub
  loc_0040B56C: 'Referenced from: 0040B556
End Sub

Public Sub Proc_1_11_40B580
  loc_0040B5D5: var_eax = Proc_1_2_40A9E0(var_38, arg_C, 1)
  loc_0040B5F4: var_40 = arg_C And 128 And 27
  loc_0040B5FE: call Xor(var_38, var_48, var_38, edi, %ecx = %S_edx_S, arg_C And 128 And 27)
  loc_0040B609: var_24 = Xor(var_38, var_48, var_24, edi, var_24 = %S_edx_S, arg_C And 128 And 27)
  loc_0040B610: GoTo loc_0040B62B
  loc_0040B616: If var_4 Then
  loc_0040B621: End If
  loc_0040B62A: Exit Sub
  loc_0040B62B: 'Referenced from: 0040B610
End Sub

Public Sub Proc_1_12_40B660
  loc_0040B699: If arg_10 = 0 Then ebx = 1
  loc_0040B6A4: If arg_C = 0 Then edx = 1
  loc_0040B6A9: If edx = 0 Then
  loc_0040B6CD:   eax+esi = eax+esi + ecx+esi
  loc_0040B6D0:   idiv ecx
  loc_0040B6DA:   var_28 = edx+eax
  loc_0040B6E4:   GoTo loc_0040B6F4
  loc_0040B6E6: End If
  loc_0040B6F4: 'Referenced from: 0040B6E4
  loc_0040B705: GoTo loc_0040B711
  loc_0040B710: Exit Sub
  loc_0040B711: 'Referenced from: 0040B705
End Sub

Public Sub Proc_1_13_40B750
  loc_0040B78F: Dim var_2C(3) As Byte
  loc_0040B7A3: var_eax = Proc_1_9_40B250(arg_C, var_2C, var_2C)
  loc_0040B7CB: var_20(1) = ecx+edx*4
  loc_0040B7DF: var_20(1) = edx+ecx*4
  loc_0040B7F3: var_20(1) = ecx+edx*4
  loc_0040B804: var_eax = Proc_1_6_40AF60(var_50, var_2C, 17)
  loc_0040B80F: var_40 = var_50
  loc_0040B81A: GoTo loc_0040B835
  loc_0040B820: If var_4 Then
  loc_0040B82B: End If
  loc_0040B834: Exit Sub
  loc_0040B835: 'Referenced from: 0040B81A
  loc_0040B83E: var_54 = var_2C
End Sub

Public Sub Proc_1_14_40B880
  loc_0040B8F2: Dim var_2C(3) As Byte
  loc_0040B8FF: Dim var_58(3) As Byte
  loc_0040B915: var_eax = Proc_1_9_40B250(arg_C, var_58, var_58)
  loc_0040B92E: var_eax = Proc_1_9_40B250(arg_10, var_2C, 4209692)
  loc_0040B93F: var_eax = Proc_1_12_40B660(var_6C, var_4C, var_20)
  loc_0040B94A: edx = var_20 + 1
  loc_0040B94C: eax = var_4C + 1
  loc_0040B952: var_eax = Proc_1_12_40B660(var_7C, var_4C + 1, var_20 + 1)
  loc_0040B96C: var_eax = Proc_1_12_40B660(var_9C, var_4C(1), var_20(1))
  loc_0040B986: var_eax = Proc_1_12_40B660(var_BC, var_4C(1), var_20(1))
  loc_0040B9A0: call Xor(var_8C, var_7C, var_6C, 00000011h, var_2C, 00403C1Ch, 00000011h, edi, Xor, ebx)
  loc_0040B9B1: call Xor(var_AC, var_9C, Xor(var_8C, var_7C, var_6C, 00000011h, var_2C, 00403C1Ch, 00000011h, edi, Xor, ebx))
  loc_0040B9C2: call Xor(var_CC, var_BC, Xor(var_AC, var_9C, Xor(var_8C, var_7C, var_6C, 00000011h, var_2C, 00403C1Ch, 00000011h, edi, Xor, ebx)))
  loc_0040B9C9: var_40 = Xor(var_CC, var_BC, Xor(var_AC, var_9C, Xor(var_8C, var_7C, var_6C, 00000011h, var_2C, 00403C1Ch, 00000011h, edi, Xor, ebx)))
  loc_0040B9F5: GoTo loc_0040BA3D
  loc_0040B9FB: If var_4 Then
  loc_0040BA06: End If
  loc_0040BA3C: Exit Sub
  loc_0040BA3D: 'Referenced from: 0040B9F5
  loc_0040BA50: var_D0 = var_2C
  loc_0040BA63: var_D4 = var_58
End Sub

Public Sub Proc_1_15_40BAA0
  loc_0040BAE5: Dim var_40(3) As Byte
  loc_0040BAFA: var_eax = Proc_1_6_40AF60(var_58, global_004110DC, var_40)
  loc_0040BB14: var_28 = CLng(var_58)
  loc_0040BB25: var_eax = Proc_1_14_40B880(var_58, var_28, arg_C)
  loc_0040BB37: var_34(1) = CByte(var_58)
  loc_0040BB52: var_eax = Proc_1_4_40AD70(var_58, var_28, &H18)
  loc_0040BB60: var_28 = CLng(var_58)
  loc_0040BB6E: var_eax = Proc_1_14_40B880(var_58, var_28, arg_C)
  loc_0040BB80: var_34(1) = CByte(var_58)
  loc_0040BB9B: var_eax = Proc_1_4_40AD70(var_58, var_28, &H18)
  loc_0040BBA9: var_28 = CLng(var_58)
  loc_0040BBB7: var_eax = Proc_1_14_40B880(var_58, var_28, arg_C)
  loc_0040BBC9: var_34(1) = CByte(var_58)
  loc_0040BBE4: var_eax = Proc_1_4_40AD70(var_58, var_28, &H18)
  loc_0040BC00: var_eax = Proc_1_14_40B880(var_58, CLng(var_58), arg_C)
  loc_0040BC09: var_ret_8 = CByte(var_58)
  loc_0040BC27: var_eax = Proc_1_6_40AF60(var_58, var_40, 4209692)
  loc_0040BC49: var_24 = CLng(var_58)
  loc_0040BC54: GoTo loc_0040BC6F
  loc_0040BC5A: If var_4 Then
  loc_0040BC65: End If
  loc_0040BC6E: Exit Sub
  loc_0040BC6F: 'Referenced from: 0040BC54
  loc_0040BC78: var_6C = var_40
End Sub

Public Sub Proc_1_16_40BCC0
  loc_0040BD01: var_18 = arg_C
  loc_0040BD0D: movzx cx, [edx+eax]
  loc_0040BD17: 000000FFh = 000000FFh - arg_C
  loc_0040BD31: var_18 = eax+ecx
  loc_0040BD3B: var_eax = Proc_1_5_40AE60(var_3C, var_18, 1)
  loc_0040BD72: var_eax = Proc_1_5_40AE60(var_3C, CByte(var_3C), 1)
  loc_0040BD9D: var_eax = Proc_1_5_40AE60(var_3C, CByte(var_3C), 1)
  loc_0040BDC8: var_eax = Proc_1_5_40AE60(var_3C, CByte(var_3C), 1)
  loc_0040BDD6: var_18 = CByte(var_3C)
  loc_0040BDF1: var_2C =
  loc_0040BDFC: GoTo loc_0040BE17
  loc_0040BE02: If var_4 Then
  loc_0040BE0D: End If
  loc_0040BE16: Exit Sub
  loc_0040BE17: 'Referenced from: 0040BDFC
End Sub

Public Sub Proc_1_17_40BE50
  loc_0040BE9D: Dim var_30(3) As Byte
  loc_0040BEE3: 
  loc_0040BEEA: If 00000002h <= 255 Then
  loc_0040BEFE:   var_60 = eax+ebx-00000001h
  loc_0040BF08:   var_eax = Proc_1_11_40B580(var_48, eax+ebx-00000001h, var_30)
  loc_0040BF19:   call Xor(var_58, var_48, var_68, 00403C1Ch, 00000011h, %S_eax_S = CByte(%StkVar1), undef 'Ignore this '__vbaFreeVar, 00000002h)
  loc_0040BF20:   var_ret_1 = CByte(Xor(var_58, var_48, var_68, 00403C1Ch, 00000011h, var_ret_1 = CByte(%StkVar1), undef)
  loc_0040BF48:   00000002h = 00000002h + 00000001h
  loc_0040BF4A:   GoTo loc_0040BEE3
  loc_0040BF4C: End If
  loc_0040BF6C: 
  loc_0040BF73: If 00000001h <= 255 Then
  loc_0040BF80:   var_eax = Proc_1_16_40BCC0(var_48, 1)
  loc_0040BF8E:   var_38 = CByte(var_48)
  loc_0040BFBB:   00000001h = 00000001h + 00000001h
  loc_0040BFBD:   GoTo loc_0040BF6C
  loc_0040BFBF: End If
  loc_0040BFC5: 
  loc_0040BFCC: If ebx <= 29 Then
  loc_0040BFE7:   var_eax = Proc_1_11_40B580(var_48, 1)
  loc_0040BFF5:   var_38 = CByte(var_48)
  loc_0040BFFF:   ebx = ebx + 00000001h
  loc_0040C001:   GoTo loc_0040BFC5
  loc_0040C003: End If
  loc_0040C01F: If ebx <= &HFF Then
  loc_0040C031:   var_38 = ecx+ebx*4
  loc_0040C034:   var_60 = ecx+ebx*4
  loc_0040C043:   var_eax = Proc_1_11_40B580(var_48, var_38)
  loc_0040C054:   call Xor(var_58, var_48, var_68)
  loc_0040C060:   var_24(1) = CByte(Xor(var_58, var_48, var_68))
  loc_0040C06E:   var_24(1) = var_38
  loc_0040C07A:   var_24(1) = var_38
  loc_0040C082:   var_eax = Proc_1_11_40B580(var_48, var_38)
  loc_0040C08B:   var_ret_5 = CByte(var_48)
  loc_0040C0A5:   var_eax = Proc_1_6_40AF60(var_48, var_30)
  loc_0040C0AE:   var_ret_6 = CLng(var_48)
  loc_0040C0D5:   var_38 = edx+ebx*4
  loc_0040C0DD:   var_eax = Proc_1_12_40B660(var_48, global_004110E8, var_38)
  loc_0040C0EE:   var_24(1) = CByte(var_48)
  loc_0040C0FD:   ecx = 004110E8h + 1
  loc_0040C103:   var_eax = Proc_1_12_40B660(var_48, 004110E8h + 1, var_38)
  loc_0040C111:   var_24(1) = CByte(var_48)
  loc_0040C122:   004110E8h = 004110E8h + 00000002h
  loc_0040C12A:   var_eax = Proc_1_12_40B660(var_48, 004110E8h+00000002h, var_38)
  loc_0040C138:   var_24(1) = CByte(var_48)
  loc_0040C149:   004110E8h = 004110E8h + 00000003h
  loc_0040C151:   var_eax = Proc_1_12_40B660(var_48, 004110E8h+00000003h, var_38)
  loc_0040C15A:   var_ret_A = CByte(var_48)
  loc_0040C174:   var_eax = Proc_1_6_40AF60(var_48, var_30)
  loc_0040C17D:   var_ret_B = CLng(var_48)
  loc_0040C191:   ebx = ebx + 1
  loc_0040C197:   GoTo loc_0040C019
  loc_0040C19C: End If
  loc_0040C1A1: GoTo loc_0040C1B7
  loc_0040C1B6: Exit Sub
  loc_0040C1B7: 'Referenced from: 0040C1A1
  loc_0040C1C0: var_6C = var_30
End Sub

Public Sub Proc_1_18_40C1E0
  loc_0040C25E: Dim var_34(7) As Variant
  loc_0040C282: global_004111C8 = Me
  loc_0040C296: global_004111B8 = arg_C
  loc_0040C2BF: If (global_004111C8 >= global_004111B8) Then
  loc_0040C2E4:   global_004111D8 = var_D0 + global_004111C8
  loc_0040C2E6:   GoTo loc_0040C311
  loc_0040C2E8: End If
  loc_0040C305: global_004111D8 = var_D0 + global_004111B8
  loc_0040C311: 'Referenced from: 0040C2E6
  loc_0040C32E: var_4C = CInt(1)
  loc_0040C359: If (global_004111C8 < var_D0) Then
  loc_0040C375:   var_60 = CInt(2)
  loc_0040C381:   GoTo loc_0040C3AC
  loc_0040C383: End If
  loc_0040C3A0: var_60 = CInt(3)
  loc_0040C3AC: 'Referenced from: 0040C381
  loc_0040C3BF: var_70 = CInt(4)
  loc_0040C3F2: var_ret_1 = Me - var_D0
  loc_0040C3FB: var_ret_2 = CLng(var_ret_1)
  loc_0040C403: var_104 = var_ret_2
  loc_0040C414: If eax <= var_ret_2 Then
  loc_0040C42E:   var_12C = eax+eax*2
  loc_0040C438:   var_3C = var_4C(var_4C*2)
  loc_0040C45A:   var_E0 = Me
  loc_0040C468:   call Mod(var_90, var_E0, var_D0 + var_4C, var_34, 00403C38h, 0000000Ch, %S_eax_S = #StkVar1%StkVar3 - %StkVar2, %S_eax_S = CLng(%StkVar1), undef 'Ignore this '__vbaFreeVar)
  loc_0040C47D:   var_12C(1066111) = Mod(var_90, var_E0, var_D0 + var_4C, var_34, 00403C38h, 0000000Ch, var_ret_3 =  - , var_ret_3 = CLng(), undef 'Ignore this '__vbaFreeVar)
  loc_0040C48E:   eax = var_3C + 1
  loc_0040C498:   var_C8 = var_18
  loc_0040C4A2:   var_130 = var_3C + 1
  loc_0040C4C7:   var_E0 = Me
  loc_0040C4D5:   call Mod(var_90, var_E0, var_D0 + var_60)
  loc_0040C4EA:   var_130(1066111) = Mod(var_90, var_E0, var_D0 + var_60)
  loc_0040C507:   var_C8 = var_18
  loc_0040C511:   var_134 = var_3C(1)
  loc_0040C536:   var_E0 = Me
  loc_0040C544:   call Mod(var_90, var_E0, var_D0 + var_70)
  loc_0040C559:   var_134(1066111) = Mod(var_90, var_E0, var_D0 + var_70)
  loc_0040C567:   var_C8 = var_18
  loc_0040C5A4:   var_ret_4 = Me + var_D0 - var_4C
  loc_0040C5B0:   var_F0 = Me
  loc_0040C5BE:   call Mod(var_A0, var_F0, var_ret_4)
  loc_0040C5D3:   var_12C(1066118) = Mod(var_A0, var_F0, var_ret_4)
  loc_0040C5E1:   var_C8 = var_18
  loc_0040C61E:   var_ret_5 = Me + var_D0 - var_60
  loc_0040C62A:   var_F0 = Me
  loc_0040C638:   call Mod(var_A0, var_F0, var_ret_5)
  loc_0040C64D:   var_130(1066118) = Mod(var_A0, var_F0, var_ret_5)
  loc_0040C65B:   var_C8 = var_18
  loc_0040C698:   var_ret_6 = Me + var_D0 - var_70
  loc_0040C6A4:   var_F0 = Me
  loc_0040C6B2:   call Mod(var_A0, var_F0, var_ret_6)
  loc_0040C6C7:   var_134(1066118) = Mod(var_A0, var_F0, var_ret_6)
  loc_0040C6DC:   var_18 = var_18(1)
  loc_0040C6DF:   GoTo loc_0040C40E
  loc_0040C6E4: End If
  loc_0040C71B: var_ret_7 = global_004111C8 * global_004111D8 + 2
  loc_0040C722: var_ret_8 = CLng(var_ret_7)
  loc_0040C727: var_50 = var_ret_8
  loc_0040C750: var_ret_9 = global_004111B8 - 2
  loc_0040C753: var_ret_A = CLng(var_ret_9)
  loc_0040C755: var_10C = var_ret_A
  loc_0040C766: If eax <= var_ret_A Then
  loc_0040C77E:   var_eax = Proc_1_8_40B150(var_80, arg_10, eax*4)
  loc_0040C78F:   var_14 = var_14 + var_28
  loc_0040C791:   ecx = var_80
  loc_0040C7A6:   var_14 = var_14(1)
  loc_0040C7AB:   GoTo loc_0040C760
  loc_0040C7AD: End If
  loc_0040C7D1: var_ret_B = global_004111B8 - 2
  loc_0040C7D4: var_ret_C = CLng(var_ret_B)
  loc_0040C7D6: var_114 = var_ret_C
  loc_0040C7E7: If eax <= var_ret_C Then
  loc_0040C7EF:   eax = eax + var_28
  loc_0040C7F2:   var_ret_D = CLng(eax+var_28)
  loc_0040C807:   var_14 = var_14(1)
  loc_0040C80C:   GoTo loc_0040C7E1
  loc_0040C80E: End If
  loc_0040C813: var_ret_E = CLng(global_004111B8)
  loc_0040C815: var_18 = var_ret_E
  loc_0040C822: If var_ret_E < var_ret_8 Then
  loc_0040C828:   var_C8 = var_ret_E
  loc_0040C848:   var_ret_F = var_D0 - global_004111B8
  loc_0040C84B:   var_ret_10 = CLng(var_ret_F)
  loc_0040C856:   var_D8 = ecx+eax*4
  loc_0040C886:   var_eax = Proc_1_4_40AD70(var_90, ecx+edx*4-00000004h, &H18)
  loc_0040C8A8:   var_eax = Proc_1_13_40B750(var_A0, CLng(var_90))
  loc_0040C8C6:   var_E8 = var_E0(var_A0*4)
  loc_0040C8DE:   call Xor(var_B0, var_A0, var_E0)
  loc_0040C8F3:   call Xor(var_C0, var_F0, Xor(var_B0, var_A0, var_E0))
  loc_0040C8FA:   var_ret_12 = CLng(Xor(var_C0, var_F0, Xor(var_B0, var_A0, var_E0)))
  loc_0040C94A:   If (global_004111B8 <= var_D0) Then
  loc_0040C958: 
  loc_0040C9C2:     var_FC = CBool((&H8003 < global_004111B8) And 11)
  loc_0040C9D2:     If var_FC = 0 Then GoTo loc_0040CC1C
  loc_0040C9E1:     var_18 = var_18 + var_14
  loc_0040C9E9:     var_C8 = eax+ecx
  loc_0040CA0C:     var_138 = var_80(var_D0*4)
  loc_0040CA12:     var_ret_15 = var_D0 - global_004111B8
  loc_0040CA15:     var_ret_16 = CLng(var_ret_15)
  loc_0040CA2E:     eax = var_14 + 1
  loc_0040CA2F:     var_14 = var_14 + 1
  loc_0040CA32:     GoTo loc_0040C958
  loc_0040CA37:   End If
  loc_0040CA45:   If 00000001h < 4 Then
  loc_0040CA4D:     If eax+edx < var_ret_8 Then
  loc_0040CA57:       var_C8 = eax+edx
  loc_0040CA7A:       var_138 = var_80(edx+eax*4*4)
  loc_0040CA80:       var_ret_17 = 3 - global_004111B8
  loc_0040CA83:       var_ret_18 = CLng(var_ret_17)
  loc_0040CA9C:       eax = var_14 + 1
  loc_0040CA9D:       var_14 = var_14 + 1
  loc_0040CAA2:       GoTo loc_0040CA3F
  loc_0040CAA4:     End If
  loc_0040CAA4:   End If
  loc_0040CAAC:   If ecx < var_ret_8 Then
  loc_0040CAB9:     var_C8 = .AddRef 'Ignore this
  loc_0040CAD2:     var_ret_19 = 3 - global_004111B8
  loc_0040CAD5:     var_ret_1A = CLng(var_ret_19)
  loc_0040CAE7:     var_D8 = ecx+eax*4
  loc_0040CAFF:     var_eax = Proc_1_13_40B750(var_90, ecx+eax*4+0000000Ch)
  loc_0040CB19:     call Xor(var_A0, var_90, var_E0)
  loc_0040CB20:     var_ret_1B = CLng(Xor(var_A0, var_90, var_E0))
  loc_0040CB3A:   End If
  loc_0040CB42: 
  loc_0040CBA9:   var_FC = CBool((&H8003 < global_004111B8) And False)
  loc_0040CBB9:   If var_FC Then
  loc_0040CBC4:     var_18 = var_18 + var_14
  loc_0040CBCC:     var_C8 = eax+ecx
  loc_0040CBEF:     var_138 = var_80(var_D0*4)
  loc_0040CBF5:     var_ret_1E = var_D0 - global_004111B8
  loc_0040CBF8:     var_ret_1F = CLng(var_ret_1E)
  loc_0040CC0E:     var_14 = var_14 + 1
  loc_0040CC17:     GoTo loc_0040CB42
  loc_0040CC1C:   End If
  loc_0040CC2F:   var_C8 = var_ret_E
  loc_0040CC46:   var_ret_20 = CLng(3 + global_004111B8)
  loc_0040CC4B:   var_18 = var_ret_20
  loc_0040CC50:   var_1C = var_1C + 1
  loc_0040CC56:   GoTo loc_0040C81F
  loc_0040CC5B: End If
  loc_0040CC7F: var_ret_21 = global_004111C8 - var_D0
  loc_0040CC82: var_ret_22 = CLng(var_ret_21)
  loc_0040CC84: var_11C = var_ret_22
  loc_0040CC95: If eax <= var_ret_22 Then
  loc_0040CCA0:   var_50 = var_50 + eax
  loc_0040CCA2:   var_C8 = var_50+eax
  loc_0040CCD6:   var_ret_23 = var_D0 - Me
  loc_0040CCD9:   var_ret_24 = CLng(var_ret_23)
  loc_0040CCF6:   GoTo loc_0040CC8C
  loc_0040CCF8: End If
  loc_0040CCFF: var_14 = CLng(global_004111C8)
  loc_0040CD02: 
  loc_0040CD0F: var_D8 = var_14
  loc_0040CD1C: var_C8 = var_50
  loc_0040CD3F: var_ret_26 = 3 - global_004111C8
  loc_0040CD4B: If (var_E0 < var_ret_26) Then
  loc_0040CD6F:   var_C8 = var_50
  loc_0040CD7E:   var_D8 = var_14
  loc_0040CD84:   var_ret_27 = 3 - global_004111C8
  loc_0040CD95:   var_ret_28 = var_ret_27 - 3
  loc_0040CDAA:   var_1C = CLng(var_ret_28)
  loc_0040CDC1:   var_ret_2A = global_004111C8 - 2
  loc_0040CDC4:   var_ret_2B = CLng(var_ret_2A)
  loc_0040CDC6:   var_124 = var_ret_2B
  loc_0040CDD7:   If eax <= var_ret_2B Then
  loc_0040CDE2:     eax = eax + var_14
  loc_0040CDEC:     var_eax = Proc_1_15_40BAA0(var_80, edx+eax*4)
  loc_0040CDF5:     var_ret_2C = CLng(var_80)
  loc_0040CDFD:     var_1C = var_1C + var_18
  loc_0040CE17:     GoTo loc_0040CDCE
  loc_0040CE19:   End If
  loc_0040CE2C:   var_C8 = var_14
  loc_0040CE43:   var_ret_2D = CLng(3 + global_004111C8)
  loc_0040CE48:   var_14 = var_ret_2D
  loc_0040CE4D:   GoTo loc_0040CD02
  loc_0040CE52: End If
  loc_0040CE65: var_C8 = var_50
  loc_0040CE75: var_ret_2E = 3 - global_004111C8
  loc_0040CE78: var_ret_2F = CLng(var_ret_2E)
  loc_0040CE7A: 
  loc_0040CE82: If var_ret_2F < var_ret_8 Then
  loc_0040CE86:   var_ret_2F = var_ret_2F - var_50
  loc_0040CE8E:   var_C8 = var_ret_2F
  loc_0040CEB8:   var_ret_30 = CLng(3 + global_004111C8)
  loc_0040CECD:   eax = var_ret_2F + 1
  loc_0040CECE:   GoTo loc_0040CE7A
  loc_0040CED0: End If
  loc_0040CED5: GoTo loc_0040CF03
  loc_0040CF02: Exit Sub
  loc_0040CF03: 'Referenced from: 0040CED5
  loc_0040CF0F: var_F4 = var_34
End Sub

Public Sub Proc_1_19_40CF50
  Dim var_174 As Me
  Dim var_70 As Me
  Dim var_64 As Me
  Dim var_6C As Me
  Dim var_68 As Me
  Dim Me As Me
  Dim var_18 As Me
  loc_0040D025: Dim var_38(7) As Long
  loc_0040D032: Dim var_54(7) As Long
  loc_0040D058: var_ret_1 = global_004111C8 - 1
  loc_0040D065: var_ret_2 = CLng(var_ret_1)
  loc_0040D067: var_190 = var_ret_2
  loc_0040D075: If ebx <= var_ret_2 Then
  loc_0040D08D:   var_eax = Proc_1_7_40B050(var_80, Me, ebx*4)
  loc_0040D096:   var_ret_3 = CLng(var_80)
  loc_0040D0BB:   ebx = ebx + 00000001h
  loc_0040D0BD:   GoTo loc_0040D06F
  loc_0040D0BF: End If
  loc_0040D0D2: var_1C = CLng(global_004111C8)
  loc_0040D0E3: var_64 = var_38
  loc_0040D0F9: var_60 = var_54
  loc_0040D120: var_ret_5 = global_004111D8 - 1
  loc_0040D127: var_ret_6 = CLng(var_ret_5)
  loc_0040D138: var_198 = var_ret_6
  loc_0040D13E: 
  loc_0040D160: If var_14 <= var_ret_6 Then
  loc_0040D171:   var_ret_7 = global_004111C8 - 1
  loc_0040D178:   var_ret_8 = CLng(var_ret_7)
  loc_0040D17A:   var_1A0 = var_ret_8
  loc_0040D18B:   If eax <= var_ret_8 Then
  loc_0040D19C:     var_20 = var_64(var_64*2)
  loc_0040D1C1:     var_ret_9 = CLng(var_20(1066118))
  loc_0040D1C8:     var_ret_9 = var_ret_9 - eax+00000014h
  loc_0040D1D6:     var_eax = Proc_1_1_40A7C0(var_80, var_174.GetTypeInfoCount, var_68)
  loc_0040D1FE:     eax = var_20 + 1
  loc_0040D20C:     var_ret_A = CLng(var_20 + 1(1066118))
  loc_0040D213:     var_ret_A = var_ret_A - eax+00000014h
  loc_0040D224:     var_eax = Proc_1_1_40A7C0(var_C0, var_174.GetTypeInfoCount, var_6C)
  loc_0040D25C:     var_ret_B = CLng(var_20(1066119))
  loc_0040D263:     var_ret_B = var_ret_B - eax+00000014h
  loc_0040D274:     var_eax = Proc_1_1_40A7C0(var_100, var_174.GetTypeInfoCount, var_70)
  loc_0040D288:     var_18 = var_18 - var_174.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_0040D2B6:     var_148 = edx+eax*4 xor [ecx+edx*4]
  loc_0040D2E4:     var_138 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D300:     var_ret_D = CLng(var_80 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D313:     var_eax = Proc_1_4_40AD70(var_A0, ecx+eax*4, 8)
  loc_0040D338:     var_158 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D35E:     var_ret_F = CLng(var_C0 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D371:     var_eax = Proc_1_4_40AD70(var_E0, ecx+eax*4, 16)
  loc_0040D396:     var_168 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D3BC:     var_ret_11 = CLng(var_100 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D3CF:     var_eax = Proc_1_4_40AD70(var_120, ecx+eax*4, &H18)
  loc_0040D3E9:     call Xor(var_B0, var_A0, var_150, var_54, 00403C54h, 00000003h, var_38, 00403C54h, 00000003h, undef 'Ignore this, %S_eax_S = CLng(%StkVar1))
  loc_0040D3FE:     call Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150, var_54, 00403C54h, 00000003h, var_38, 00403C54h, 00000003h, undef)
  loc_0040D413:     call Xor(var_130, var_120, Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150, var_54, 00403C54h, 00000003h, var_38, 00403C54h, 00000003h, undef))
  loc_0040D41A:     var_ret_12 = CLng(Xor(var_130, var_120, Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150, var_54, 00403C54h, 00000003h, var_38, 00403C54h, 00000003h, undef)))
  loc_0040D422:     var_18 = var_18 - ecx+00000014h
  loc_0040D460:     eax = var_1C + 1
  loc_0040D461:     var_1C = var_1C + 1
  loc_0040D46E:     GoTo loc_0040D182
  loc_0040D473:   End If
  loc_0040D489:   var_64 = var_60
  loc_0040D497:   var_60 = var_64
  loc_0040D4A7:   var_14 = var_14(1)
  loc_0040D4AA:   GoTo loc_0040D13E
  loc_0040D4AF: End If
  loc_0040D4BA: var_ret_13 =  - var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D4C1: var_ret_14 = CLng(var_ret_13)
  loc_0040D4C3: var_1A8 = var_ret_14
  loc_0040D4D4: If eax <= var_ret_14 Then
  loc_0040D4E5:   var_20 = var_68(var_68*2)
  loc_0040D50A:   var_ret_15 = CLng(var_20(1066118))
  loc_0040D511:   var_ret_15 = var_ret_15 - eax+00000014h
  loc_0040D51F:   var_eax = Proc_1_1_40A7C0(var_80, var_174.GetTypeInfoCount, var_68)
  loc_0040D547:   eax = var_20 + 1
  loc_0040D555:   var_ret_16 = CLng(var_20 + 1(1066118))
  loc_0040D55C:   var_ret_16 = var_ret_16 - eax+00000014h
  loc_0040D56D:   var_eax = Proc_1_1_40A7C0(var_C0, var_174.GetTypeInfoCount, var_6C)
  loc_0040D5A5:   var_ret_17 = CLng(var_20(1066119))
  loc_0040D5AC:   var_ret_17 = var_ret_17 - eax+00000014h
  loc_0040D5BD:   var_eax = Proc_1_1_40A7C0(var_100, var_174.GetTypeInfoCount, var_70)
  loc_0040D5D1:   var_18 = var_18 - var_174.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_0040D5FF:   var_148 = edx+eax*4 xor [ecx+edx*4]
  loc_0040D62D:   var_138 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D649:   var_ret_19 = CLng(var_80 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D65C:   var_eax = Proc_1_4_40AD70(var_A0, ecx+eax*4, 8)
  loc_0040D681:   var_158 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D6A7:   var_ret_1B = CLng(var_C0 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D6BA:   var_eax = Proc_1_4_40AD70(var_E0, ecx+eax*4, 16)
  loc_0040D6DF:   var_168 = var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2)
  loc_0040D705:   var_ret_1D = CLng(var_100 And var_174.%x3 = PropBag.ReadProperty(%StkVar1, %StkVar2))
  loc_0040D718:   var_eax = Proc_1_4_40AD70(var_120, ecx+eax*4, &H18)
  loc_0040D732:   call Xor(var_B0, var_A0, var_150)
  loc_0040D747:   call Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150))
  loc_0040D75C:   call Xor(var_130, var_120, Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150)))
  loc_0040D763:   var_ret_1E = CLng(Xor(var_130, var_120, Xor(var_F0, var_E0, Xor(var_B0, var_A0, var_150))))
  loc_0040D76B:   var_18 = var_18 - ecx+00000014h
  loc_0040D7A9:   eax = var_1C + 1
  loc_0040D7AA:   var_1C = var_1C + 1
  loc_0040D7B7:   GoTo loc_0040D4CB
  loc_0040D7BC: End If
  loc_0040D7E0: var_ret_1F = global_004111C8 - 1
  loc_0040D7E7: var_ret_20 = CLng(var_ret_1F)
  loc_0040D7E9: var_1B0 = var_ret_20
  loc_0040D7F7: If esi <= var_ret_20 Then
  loc_0040D808:   var_18 = esi*4
  loc_0040D81D:   esi = esi - var_174.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_0040D826:   var_eax = Proc_1_10_40B3E0(var_174.GetTypeInfoCount, var_68, var_60)
  loc_0040D85E:   esi-var_174.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this = esi-var_174.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this + 00000001h
  loc_0040D860:   GoTo loc_0040D7F1
  loc_0040D862: End If
  loc_0040D867: GoTo loc_0040D8DE
  loc_0040D8DD: Exit Sub
  loc_0040D8DE: 'Referenced from: 0040D867
  loc_0040D8F0: var_174 = var_38
  loc_0040D904: var_178 = var_54
End Sub

Public Sub Proc_1_20_40D940
  loc_0040D98E: On Error Resume Next
  loc_0040D99F: call __vbaRefVarAry(arg_C, FFFFFFFFh, edi, esi, ebx)
  loc_0040D9AA: call UBound(00000001h, __vbaRefVarAry(arg_C, FFFFFFFFh, edi, esi, ebx))
  loc_0040D9B0: var_38 = UBound(00000001h, __vbaRefVarAry(arg_C, FFFFFFFFh, edi, esi, ebx))
  loc_0040D9D5: var_30 = IsNumeric(UBound(00000001h, __vbaRefVarAry(arg_C, FFFFFFFFh, edi, esi, ebx)))
  loc_0040D9E9: GoTo loc_0040DA08
  loc_0040D9F3: If 0 And 4 Then
  loc_0040D9FE: End If
  loc_0040DA07: Exit Sub
  loc_0040DA08: 'Referenced from: 0040D9E9
End Sub

Public Sub Proc_1_21_40DA40
  loc_0040DA98: GoTo loc_0040DA9F
  loc_0040DA9A: 
  loc_0040DA9F: 'Referenced from: 0040DA98
  loc_0040DAA7: var_48 = arg_14
  loc_0040DABC: var_58 = arg_C
  loc_0040DACE: var_ret_1 = CLng(arg_14 + var_20)
  loc_0040DAE8: var_68 = var_ret_1
  loc_0040DAF0: var_ret_2 = CLng(arg_C + var_20)
  loc_0040DB41: var_20 = var_20 + 1
  loc_0040DB67: If (var_20 = arg_18) = 0 Then GoTo loc_0040DA9A
  loc_0040DB72: GoTo loc_0040DB88
  loc_0040DB87: Exit Sub
  loc_0040DB88: 'Referenced from: 0040DB72
End Sub

Public Sub Proc_1_22_40DBB0
  loc_0040DC22: Dim var_2C(3) As Byte
  loc_0040DC2F: Dim var_50(31) As Byte
  loc_0040DC3C: Dim var_80(31) As Byte
  loc_0040DC5F: var_eax = Proc_1_20_40D940(var_94, &H6011, var_80)
  loc_0040DC78: call Not(var_A4, var_94, 00403C70h, 00000011h, var_50, 00403C70h, 00000011h, var_2C, 00403C1Ch, 00000011h, %sa, esi, Not)
  loc_0040DC92: If CBool(Not(var_A4, var_94, 00403C70h, 00000011h, var_50, 00403C70h, 00000011h, var_2C, 00403C1Ch, 00000011h, %sa, esi, Not)) = 0 Then
  loc_0040DCA9:   var_AC = arg_C
  loc_0040DCB9:   var_eax = Proc_1_20_40D940(var_94, &H6011)
  loc_0040DCCC:   call Not(var_A4, var_94)
  loc_0040DCE6:   If CBool(Not(var_A4, var_94)) = 0 Then
  loc_0040DCF4:     call UBound(00000001h, Me)
  loc_0040DCFC:     ebx = UBound(00000001h, Me) + 1
  loc_0040DD05:     If Not Sign(-2147483617 - 0) Then
  loc_0040DD07:       edx = -2147483617 - 1
  loc_0040DD0B:       edx = -32 + 1
  loc_0040DD0C:     End If
  loc_0040DD0C:     If -32 + 1 = 0 Then
  loc_0040DD17:       call UBound(00000001h, arg_C)
  loc_0040DD1D:       var_DC = UBound(00000001h, arg_C)
  loc_0040DD38:       If ecx <= UBound(00000001h, arg_C) Then
  loc_0040DD51:         If var_5C <> 31 Then
  loc_0040DD53:           var_5C = var_5C + 1
  loc_0040DD59:           GoTo loc_0040DD2F
  loc_0040DD5B:         End If
  loc_0040DD5B:       End If
  loc_0040DD5B:       var_eax = Proc_1_17_40BE50
  loc_0040DDA0:       var_eax = Proc_1_18_40C1E0(2, 2, var_80)
  loc_0040DDCE:       ReDim var_38(0 To ebx-00000001h)
  loc_0040DDE2:       If var_5C <= 0 Then
  loc_0040DE1E:         var_eax = Proc_1_21_40DA40(var_50, var_CC, Me)
  loc_0040DE33:         var_eax = Proc_1_19_40CF50(var_50, var_5C, &H20)
  loc_0040DE49:         var_C8 = var_50
  loc_0040DE6E:         var_eax = Proc_1_21_40DA40(var_38, var_5C, var_C8)
  loc_0040DE76:         GoTo loc_0040DDDF
  loc_0040DE7B:       End If
  loc_0040DE94:       ReDim var_64(0 To 31)
  loc_0040DEC3:       var_eax = Proc_1_21_40DA40(var_64, var_C8, var_38)
  loc_0040DED0:       var_68 = var_64
  loc_0040DED6:     End If
  loc_0040DED6:   End If
  loc_0040DED6: End If
  loc_0040DEDB: GoTo loc_0040DF09
  loc_0040DEE1: If var_4 Then
  loc_0040DEEF: End If
  loc_0040DF08: Exit Sub
  loc_0040DF09: 'Referenced from: 0040DEDB
  loc_0040DF1C: var_C8 = var_2C
  loc_0040DF36: var_CC = var_50
  loc_0040DF50: var_D0 = var_80
End Sub

Public Sub Proc_1_23_40E280
  loc_0040E2C3: If arg_C = 0 Then
  loc_0040E2D0:   GoTo loc_0040E414
  loc_0040E2D5: End If
  loc_0040E2D9: If arg_C = 31 Then
  loc_0040E2F0:   var_14 = -2147483648
  loc_0040E2F3:   GoTo loc_0040E414
  loc_0040E2F8: End If
  loc_0040E2FB: If arg_C >= 0 Then
  loc_0040E301:   If arg_C <= 31 Then GoTo loc_0040E38D
  loc_0040E351: Err = CInt(6)
  loc_0040E38D: 
  loc_0040E398: 0000001Fh = 0000001Fh - arg_C
  loc_0040E3A6: If [eax+edx] Then
  loc_0040E3B3:   0000001Eh = 0000001Eh - arg_C
  loc_0040E3C9:   var_14 = -2147483648
  loc_0040E3D1:   GoTo loc_0040E414
  loc_0040E3D3: End If
  loc_0040E3E1: arg_C = arg_C * edx+ecx*4
  loc_0040E3E5: var_14 = arg_C
  loc_0040E3ED: GoTo loc_0040E414
  loc_0040E413: Exit Sub
  loc_0040E414: 'Referenced from: 0040E2D0
End Sub
