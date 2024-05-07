VERSION 5.00
Begin VB.Form FrmMain
  Caption = "amib - RegisterMe"
  ScaleMode = 1
  AutoRedraw = False
  FontTransparent = True
  BorderStyle = 1 'Fixed Single
  'Icon = n/a
  LinkTopic = "Form1"
  MaxButton = 0   'False
  MinButton = 0   'False
  ClientLeft = 45
  ClientTop = 375
  ClientWidth = 5265
  ClientHeight = 2595
  StartUpPosition = 3 'Windows Default
  Begin Timer tmrRefresh
    Interval = 1105
    Left = 3840
    Top = 2160
  End
  Begin CommandButton cmdButton
    Index = 1
    Left = 13080
    Top = 9840
    Width = 255
    Height = 255
    TabIndex = 8
  End
  Begin CommandButton cmdButton
    Index = 0
    Left = 12720
    Top = 9840
    Width = 255
    Height = 255
    TabIndex = 7
  End
  Begin Timer tmrTalkToRemote
    Interval = 800
    Left = 3840
    Top = 1680
  End
  Begin Timer tmrRegistration
    Enabled = 0   'False
    Interval = 500
    Left = 4560
    Top = 1680
  End
  Begin TextBox txtRegKey
    Left = 1680
    Top = 1200
    Width = 3255
    Height = 285
    TabIndex = 6
  End
  Begin TextBox txtMachineCode
    Left = 1680
    Top = 720
    Width = 3255
    Height = 285
    Enabled = 0   'False
    TabIndex = 4
  End
  Begin TextBox txtUsername
    Left = 1680
    Top = 240
    Width = 3255
    Height = 285
    TabIndex = 2
  End
  Begin CommandButton CmdConfirm
    Caption = "Register"
    Left = 240
    Top = 1800
    Width = 1335
    Height = 615
    TabIndex = 0
  End
  Begin Label lblRegCode
    Caption = "Registration Key:"
    Left = 0
    Top = 1200
    Width = 1455
    Height = 375
    TabIndex = 5
    Alignment = 1 'Right Justify
  End
  Begin Label lblMachineCode
    Caption = "Machine code:"
    Left = 120
    Top = 720
    Width = 1335
    Height = 255
    TabIndex = 3
    Alignment = 1 'Right Justify
  End
  Begin Label lblUsername
    Caption = "User name:"
    Left = 120
    Top = 240
    Width = 1335
    Height = 375
    TabIndex = 1
    Alignment = 1 'Right Justify
  End
End

Attribute VB_Name = "FrmMain"

'VA: 402B58
Private Declare Function GetLastError Lib "kernel32" Alias "GetLastError" () As Long
'VA: 402B10
Private Declare Function VirtualProtect Lib "kernel32" Alias "VirtualProtect" (lpAddress As Any, ByVal dwSize As Long, ByVal flNewProtect As Long, lpflOldProtect As Long) As Long
'VA: 402AC8
Private Declare Sub CallWindowProcW Lib "user32"()
'VA: 402A70
Private Declare Function VirtualAlloc Lib "kernel32" Alias "VirtualAlloc" (lpAddress As Any, ByVal dwSize As Long, ByVal flAllocationType As Long, ByVal flProtect As Long) As Long
'VA: 402A28
Private Declare Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" (Destination As Any, Source As Any, ByVal Length As Long)


Private Sub tmrTalkToRemote_Timer() '407E10
  Dim Me As Variant
  Dim var_78 As TextBox
  loc_0040819F: On Error Resume Next
  loc_004081AD: If %x1 = Me.Height = 0 Then
  loc_00408397:   var_208 = Chr(77) & Chr(83) & Chr(88) & Chr(77) & Chr(76) & Chr(50) & Chr(46) & Chr(83) & Chr(101) & Chr(114) & Chr(118) & Chr(101) & Chr(114)
  loc_00408466:   var_50 = var_208 & Chr(88) & Chr(77) & Chr(76) & Chr(72) & Chr(84) & Chr(84) & Chr(80) & Chr(46) & Chr(54) & Chr(46) & Chr(48)
  loc_004085E4:   Set var_28 = CreateObject(var_50, 0)
  loc_0040861A:   var_60 = txtUsername.Text
  loc_0040867A:   var_60 = txtMachineCode.Text
  loc_004086DA:   var_60 = txtRegKey.Text
  loc_0040870B:   var_24 = var_60
  loc_00408724:   var_eax = FrmMain.Proc_0_18_407C20(Me, var_54, var_60, var_78, Me, Me)
  loc_00408738:   var_eax = FrmMain.Proc_0_18_407C20(Me, var_24, var_70, var_78, Me)
  loc_00408752:   var_64 = "u=" & var_60
  loc_00408765:   var_68 = var_64 & "&m="
  loc_0040879C:   var_34 = var_68 & var_58 & "&r=" & var_70
  loc_00408B2A:   var_1E8 = Chr(104) & Chr(116) & Chr(116) & Chr(112) & Chr(58) & Chr(47) & Chr(47) & Chr(97) & Chr(109) & Chr(105) & Chr(98) & Chr(45)
  loc_00408BE5:   var_348 = var_1E8 & Chr(51) & Chr(114) & Chr(108) & Chr(107) & Chr(106) & Chr(97) & Chr(118) & Chr(120) & Chr(110) & Chr(108) & Chr(51)
  loc_00408CA0:   var_4A8 = var_348 & Chr(52) & Chr(46) & Chr(115) & Chr(104) & Chr(101) & Chr(108) & Chr(108) & Chr(119) & Chr(101) & Chr(112) & Chr(108)
  loc_00408D5B:   var_608 = var_4A8 & Chr(97) & Chr(121) & Chr(97) & Chr(103) & Chr(97) & Chr(46) & Chr(109) & Chr(101) & Chr(47) & Chr(99) & Chr(104)
  loc_00408E16:   var_768 = var_608 & Chr(101) & Chr(99) & Chr(107) & Chr(95) & Chr(114) & Chr(101) & Chr(103) & Chr(105) & Chr(115) & Chr(116) & Chr(114)
  loc_00408E8A:   var_40 = var_768 & Chr(97) & Chr(116) & Chr(105) & Chr(111) & Chr(110) & Chr(63)
End Sub

Private Sub tmrRefresh_Timer() '407AE0
  loc_00407B30: ecx = "<RSAKeyValue><Modulus>SlwwwNRtDUN4mK3ORGsA79MtNWOxjyxuB0zS/W2t7MOKE+NBCG1FVoFjSlOrG138Qd1oJSwFGOrugobAG/flot+mnbBo7+wuxi4NBgLn6hNsWHaXJzwIeASdQooQ7/gj7uuBBX0h342na7/YKH0AUe/cHi7SPMYUnQk71zp5QAAU1EZIMMcFey/+l+PUV0B2uc8OnZv4x8R0B28BJPjchb9O1D7rVzvYQRXZ1sHRqWBakS4zN2d71tZX5quRwKFZ49wMQ9EwFmy5Hd1wbR0borzsu32R92YWEnIZ+RsM+PzD5glF6YFLwuO3WS0MnD/AxVjQLabWZU/iRhGkZNmrfQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
  loc_00407B50: tmrRefresh.Enabled = edi
  loc_00407B79: GoTo loc_00407B85
  loc_00407B84: Exit Sub
  loc_00407B85: 'Referenced from: 00407B79
End Sub

Private Sub tmrRegistration_Timer() '407BB0
  loc_00407BF0: [esi+00000088h] = [esi+00000088h] + 1
End Sub

Private Sub CmdConfirm_Click() '404100
  Dim Me As Variant
  Dim var_48 As TextBox
  Dim var_58 As Variant
  loc_004041B9: var_40 = txtUsername.Text
  loc_004041E6: var_30 = var_40
  loc_00404212: var_40 = txtMachineCode.Text
  loc_0040423F: var_3C = var_40
  loc_0040426B: var_40 = txtRegKey.Text
  loc_004042D4: var_68 = StrConv("nautilus", 128, 0)
  loc_004042F6: var_38 = var_68
  loc_0040430F: var_eax = Proc_40DF70(var_48, Me, Me)
  loc_0040433A: var_44 = var_30 & global_00402C34 & var_3C
  loc_00404340: var_eax = Proc_2_3_40EC00(var_44, var_48, Me)
  loc_0040434A: var_2C = Proc_2_3_40EC00(var_44, var_48, Me)
  loc_00404375: var_eax = FrmMain.Proc_0_9_404790(Me, var_24, var_1C, var_30 & global_00402C34, var_D0, Me)
  loc_00404382: If var_D0 = 0 Then
  loc_004043DE:   MsgBox(":(", 0, var_68, var_78, var_88)
  loc_00404402:   [esi+0000008Ah] = [esi+0000008Ah] + 1
  loc_00404409:   GoTo loc_004046D0
  loc_0040440E: End If
  loc_0040440E: var_eax = Proc_40A230(var_48, Me, Me)
  loc_00404413: 
  loc_00404420: If Len(var_24) < 32 Then
  loc_0040442A:   var_94 = var_24
  loc_00404461:   var_24 = var_24 & Chr(0)
  loc_00404476:   GoTo loc_00404413
  loc_00404478: End If
  loc_00404492: var_94 = var_24
  loc_004044C0: var_34 = StrConv(var_24, 128, 0)
  loc_004044D7: call Proc_1_22_40DBB0(var_34, var_38, var_34 = %S_edx_S)
  loc_004044ED: var_28 = var_38
  loc_00404504: var_94 = var_28
  loc_00404514: var_58 = StrConv(var_28, 64, 0)
  loc_00404568: If (var_58 <> var_2C) Then
  loc_0040458B:   var_58 = ":("
  loc_004045A5:   MsgBox(var_58, 0, var_68, var_78, var_88)
  loc_004045C9:   [esi+0000008Ah] = [esi+0000008Ah] + 1
  loc_004045D9:   If esi+0000008Ah <> 4096 Then GoTo loc_004046D0
  loc_004045E6:   var_eax = FrmMain.Proc_0_11_404F50(Me, var_58)
  loc_004045F5:   GoTo loc_004046D0
  loc_004045FA: End If
  loc_00404617: var_58 = "Thank you for registering this copy of amib!"
  loc_00404631: MsgBox(var_58, 0, var_68, var_78, var_88)
  loc_00404670: tmrRegistration.Enabled = True
  loc_004046AD: CmdConfirm.Enabled = ebx
  loc_004046D0: 'Referenced from: 00404409
  loc_004046D8: GoTo loc_00404724
  loc_00404723: Exit Sub
  loc_00404724: 'Referenced from: 004046D8
End Sub

Private Sub cmdButton_Click() '403FD0
  Dim Me As Me
  Dim var_18 As Me
  loc_0040401E: var_eax = FrmMain.Proc_0_14_406F60(Me, arg_C, edi)
  loc_0040402C: cwd
  loc_0040402E: idiv [esi+0000008Ch]
  loc_00404038: If Me > 0 Then
  loc_0040403C:   ecx = arg_C - 1
  loc_0040403D:   var_18 = arg_C - 1
  loc_00404045:   var_eax = FrmMain.Proc_0_14_406F60(Me, var_18)
  loc_0040404B: End If
  loc_0040405A: cwd
  loc_0040405C: idiv cx
  loc_0040405F: ecx = Me.Height = %x1s - 1
  loc_00404063: If Me < 0 Then
  loc_0040406B:   ebx = arg_C + 1
  loc_0040406D:   var_18 = arg_C + 1
  loc_00404070:   var_eax = FrmMain.Proc_0_14_406F60(Me, var_18)
  loc_00404076: End If
  loc_00404087: cwd
  loc_00404089: idiv bx
  loc_0040408F: If arg_C > 0 Then
  loc_00404097:   var_18 = arg_C
  loc_0040409D:   var_eax = FrmMain.Proc_0_14_406F60(Me)
  loc_004040A3: End If
  loc_004040B2: cwd
  loc_004040B4: idiv cx
  loc_004040BD: If arg_C < 0 Then
  loc_004040C1:   Me.Height = %x1s = Me.Height = %x1s + arg_C
  loc_004040CB:   var_eax = FrmMain.Proc_0_14_406F60(Me)
  loc_004040D1: End If
End Sub

Private Sub Form_Load() '407A40
  Dim Me As Me
  loc_00407A90: ecx = "<RSAKeyValue><Modulus>jocqo/y7eL0ZSnITk79oNyHrTlaBcJwVlM98dGDlQjZcO+UNYGKFD0BVQiO3QjWym7aIOqjf/ERfaeQpV49sLFypuT6vzKvwnJ2JFWLghB+GqQET5XVMfomz/MFP7+e7eZ5hD7mKp1HP+YSja8/47O97fislxYFzNZJCxpZuTp9+jbXsFDYrfybxNZylnQrOfyAmoNyYcRAenewdfDVltxwjMu3e0M9h4cWNSpzsopWXjM5ZWCENu/6tSTJkg9bAe7Tx9gLlMs8tpxnUqrd7snyKFK/FldJvPP2mmdSvOV1HFVk6RA0azzVo6G9fAQIJADj65b+OyhRDTVEroSxXIQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
  loc_00407A9D: var_eax = FrmMain.Proc_0_17_407750(Me, var_24)
  loc_00407AB4: GoTo loc_00407AC0
  loc_00407ABF: Exit Sub
  loc_00407AC0: 'Referenced from: 00407AB4
End Sub

Public Function LShift(num, shifts) '407340
  loc_00407398: call __vbaPowerR8(esi, global_40000000, shifts, var_28, edi, esi, ebx)
  loc_004073AF: var_18 = CLng((( * eax) * eax))
End Function

Public Function RShift(num, shifts) '4073E0
  loc_00407438: call __vbaPowerR8(esi, global_40000000, shifts, var_28, edi, esi, ebx)
  loc_0040744C: idiv ecx
  loc_0040744E: var_18 = num
End Function

Public Sub Proc_0_8_403F40
  loc_00403F47: .AddRef 'Ignore this = .AddRef 'Ignore this + 00000034h
  loc_00403F4C: If .SaveProp 'Ignore this = 0 Then
  loc_00403F93: End If
  loc_00403FAA: var_eax = CallWindowProcW(VarPtr(.AddRef), 000004D5h)
End Sub

Public Sub Proc_0_9_404790
  Dim global_00404A84 As Me
  Dim var_28 As Me
  Dim var_2C As Me
  Dim var_30 As Me
  Dim var_34 As Me
  Dim var_18 As Me
  loc_00404807: var_58 = Split(arg_14, &H402FA4, -1, 0)
  loc_00404827: var_18 = var_58
  loc_00404846: call UBound(00000001h, var_18, 0, esi, ebx)
  loc_0040484F: If UBound(00000001h, var_18, 0, esi, ebx) Then
  loc_00404859:   GoTo loc_00404A77
  loc_0040485E: End If
  loc_00404872: If esi <= 5 Then
  loc_0040487D:   esi = esi - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_0040488F:   If Len(global_00404A84.GetTypeInfoCount) <> 8 Then GoTo loc_00404851
  loc_00404891:   esi-global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this = esi-global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this + 1
  loc_00404897:   GoTo loc_0040486F
  loc_00404899: End If
  loc_004048C1: var_28 = global_00404A84.GetTypeInfoCount & global_00404A84.AddRef
  loc_004048CF: 00000002h = 00000002h - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_004048DF: var_2C =  & global_00404A84.GetTypeInfoCount
  loc_004048ED: 00000003h = 00000003h - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_004048FD: var_30 =  & global_00404A84.GetTypeInfoCount
  loc_0040490B: 00000004h = 00000004h - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_0040491B: var_34 =  & global_00404A84.GetTypeInfoCount
  loc_00404929: 00000005h = 00000005h - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_00404939: var_38 =  & global_00404A84.GetTypeInfoCount
  loc_0040494D: var_eax = FrmMain.Proc_0_10_404AB0(Me, arg_C)
  loc_0040495D: var_1C = var_7C
  loc_0040497D: If var_1C = 0 Then
  loc_0040498B:   GoTo loc_00404A77
  loc_00404990: End If
  loc_0040499C: If Len(arg_C) > 32 Then
  loc_004049BA:   var_60 = arg_C
  loc_004049D8:   arg_C = Mid(arg_C, 1, 32)
  loc_004049ED: End If
  loc_00404A0F: 00000006h = 00000006h - global_00404A84.%x1 = GetIDsOfNames(%StkVar2) 'Ignore this
  loc_00404A1A: var_eax = FrmMain.Proc_0_10_404AB0(Me, arg_10, global_00404A84.GetTypeInfoCount, var_7C)
  loc_00404A38: var_20 = var_7C
  loc_00404A3B: GoTo loc_00404A77
  loc_00404A76: Exit Sub
  loc_00404A77: 'Referenced from: 00404859
End Sub

Public Sub Proc_0_10_404AB0
  loc_00404B16: Dim var_74(63) As Byte
  loc_00404B26: Dim var_94(127) As Byte
  loc_00404B3C: var_CC = Asc(global_00402FB4)
  loc_00404B4B: If Asc(global_00402FAC) <= Asc(global_00402FB4) Then
  loc_00404B5B:   esi = esi + 1
  loc_00404B5C:   Asc(global_00402FAC) = Asc(global_00402FAC) + 00000001h
  loc_00404B5E:   GoTo loc_00404B44
  loc_00404B60: End If
  loc_00404B6C: var_D4 = Asc(global_00402FC4)
  loc_00404B7B: If Asc(global_00402FBC) <= Asc(global_00402FC4) Then
  loc_00404B8B:   esi = esi + 1 + 1
  loc_00404B8C:   Asc(global_00402FBC) = Asc(global_00402FBC) + 00000001h
  loc_00404B8E:   GoTo loc_00404B74
  loc_00404B90: End If
  loc_00404B9C: var_DC = Asc(global_00402FD4)
  loc_00404BAB: If Asc(global_00402FCC) <= Asc(global_00402FD4) Then
  loc_00404BBB:   esi = esi + 1 + 1 + 1
  loc_00404BBC:   Asc(global_00402FCC) = Asc(global_00402FCC) + 00000001h
  loc_00404BBE:   GoTo loc_00404BA4
  loc_00404BC0: End If
  loc_00404BDA: esi = esi + 1 + 1 + 1 + 1
  loc_00404BF0: If eax <= 127 Then
  loc_00404BFF:   eax = eax + 00000001h
  loc_00404C01:   GoTo loc_00404BED
  loc_00404C03: End If
  loc_00404C0D: If eax <= 63 Then
  loc_00404C28:   eax = eax + 00000001h
  loc_00404C2A:   GoTo loc_00404C0A
  loc_00404C2C: End If
  loc_00404C44: var_B4 = arg_10
  loc_00404C79: var_5C = StrConv(arg_10, 128, 0)
  loc_00404C91: call UBound(00000001h, var_5C, var_94, 00403010h, 00000011h, var_74, 00402FF4h, 00000011h, var_68, 0000003Fh, ebx)
  loc_00404C99: edi = UBound(00000001h, var_5C, var_94, 00403010h, 00000011h, var_74, 00402FF4h, 00000011h, var_68, 0000003Fh, ebx) + 1
  loc_00404CA2: If Not Sign(-2147483645 - 0) Then
  loc_00404CA4:   edx = -2147483645 - 1
  loc_00404CA8:   edx = -4 + 1
  loc_00404CA9: End If
  loc_00404CA9: If -4 + 1 Then
  loc_00404CAB: 
  loc_00404CB7:   GoTo loc_00404EE6
  loc_00404CBC: End If
  loc_00404CBE: If UBound(00000001h, var_5C, var_94, 00403010h, 00000011h, var_74, 00402FF4h, 00000011h, var_68, 0000003Fh, ebx) + 1 > 0 Then
  loc_00404CD4:   movzx cx, [edx+edi-00000001h]
  loc_00404CDD:   If var_5C = 0 Then
  loc_00404CDF:     edi = UBound(00000001h, var_5C, var_94, 00403010h, 00000011h, var_74, 00402FF4h, 00000011h, var_68, 0000003Fh, ebx) + 1 - 1
  loc_00404CE0:     GoTo loc_00404CBC
  loc_00404CE2:   End If
  loc_00404CE2: End If
  loc_00404CE9: edi+edi*2 = edi+edi*2 + 0 And 3
  loc_00404CF0: var_40 = edi+edi*2+0 And 3
  loc_00404CF3: eax = edi+edi*2+0 And 3 - 1
  loc_00404D04: ReDim var_54(0 To edi+edi*2+0 And 3 - 1)
  loc_00404D0D: GoTo loc_00404D12
  loc_00404D0F: 
  loc_00404D12: 'Referenced from: 00404D0D
  loc_00404D14: If var_3C < 0 Then
  loc_00404D26:   ebx = var_3C + 1
  loc_00404D27:   var_38 = eax+ebx
  loc_00404D2D:   ebx = var_3C + 1 + 1
  loc_00404D30:   var_44 = eax+ebx
  loc_00404D33:   var_3C = var_3C + 1 + 1
  loc_00404D36:   If var_3C + 1 + 1 < 0 Then
  loc_00404D3B:     ebx = var_3C + 1 + 1 + 1
  loc_00404D3C:     var_48 = eax+ebx
  loc_00404D3F:     var_3C = var_3C + 1 + 1 + 1
  loc_00404D42:     GoTo loc_00404D55
  loc_00404D44:   End If
  loc_00404D52:   var_48 = Asc(global_00402FAC)
  loc_00404D55:   'Referenced from: 00404D42
  loc_00404D57:   If var_3C + 1 + 1 + 1 < 0 Then
  loc_00404D62:     ebx = var_3C + 1 + 1 + 1 + 1
  loc_00404D63:     var_4C = edx+ebx
  loc_00404D66:     var_3C = var_3C + 1 + 1 + 1 + 1
  loc_00404D69:     GoTo loc_00404D79
  loc_00404D6B:   End If
  loc_00404D76:   var_4C = Asc(global_00402FAC)
  loc_00404D79:   'Referenced from: 00404D69
  loc_00404D7D:   If var_38 > 127 Then GoTo loc_00404CAB
  loc_00404D87:   If var_44 > 127 Then GoTo loc_00404CAB
  loc_00404D91:   If var_48 > 127 Then GoTo loc_00404CAB
  loc_00404D99:   If Asc(global_00402FAC) > 127 Then GoTo loc_00404CAB
  loc_00404DD6:   var_2C = ecx+esi
  loc_00404DD9:   If eax+esi > 63 Then GoTo loc_00404CAB
  loc_00404DE2:   If ecx+esi > 63 Then GoTo loc_00404CAB
  loc_00404DEB:   If ecx+esi > 63 Then GoTo loc_00404CAB
  loc_00404DF4:   If ebx+esi > 63 Then GoTo loc_00404CAB
  loc_00404E12:   var_54(4) = var_54(4) - esi+00000014h
  loc_00404E1E:   esi = var_1C + 1
  loc_00404E21:   var_1C = var_1C + 1
  loc_00404E24:   If var_1C + 1 >= edi+edi*2+0 And 3 Then GoTo loc_00404D0F
  loc_00404E3E:   var_54(4) = var_54(4) - eax+00000014h
  loc_00404E47:   esi = var_1C + 1 + 1
  loc_00404E4A:   var_1C = var_1C + 1 + 1
  loc_00404E4D:   If var_1C + 1 + 1 >= edi+edi*2+0 And 3 Then GoTo loc_00404D0F
  loc_00404E5F:   var_54(4) = var_54(4) - var_54(6)
  loc_00404E64:   eax = var_1C + 1
  loc_00404E65:   var_1C = var_1C + 1
  loc_00404E68:   GoTo loc_00404D0F
  loc_00404E6D: End If
  loc_00404E82: var_B4 = var_54
  loc_00404EAA: arg_C = StrConv(var_54, 64, 0)
  loc_00404EC8: GoTo loc_00404EE6
  loc_00404EE5: Exit Sub
  loc_00404EE6: 'Referenced from: 00404CB7
  loc_00404F08: var_C0 = var_74
  loc_00404F1F: var_C4 = var_94
End Sub

Public Sub Proc_0_11_404F50
  Dim arg_C As TextBox
  loc_00404FB8: var_30 = txtRegKey.Text
  loc_00404FF2: var_eax = FrmMain.Proc_0_12_405170(Me, var_30, var_48, var_38, arg_C)
  loc_00405031: var_eax = FrmMain.Proc_0_13_406650(Me, var_48, var_48, Me)
  loc_0040503B: var_48 = CInt(0)
  loc_0040504C: If var_48 = 1 Then
  loc_0040509F:   var_30 = CStr(Chr(58) & Chr(41))
  loc_004050A7:   var_eax = Unknown_VTable_Call[ebx+00000054h]
  loc_004050DF: End If
  loc_004050E4: GoTo loc_00405129
  loc_004050EA: If var_4 Then
  loc_004050F5: End If
  loc_00405128: Exit Sub
  loc_00405129: 'Referenced from: 004050E4
End Sub

Public Sub Proc_0_12_405170
  loc_004054E5: var_4C = Chr(178)
  loc_004054F0: var_5C = Chr(234)
  loc_004054FB: var_7C = Chr(154)
  loc_00405806: var_6C = var_4C & var_5C
  loc_004058CF: var_1EC = var_6C & var_7C & Chr(202) & Chr(122) & Chr(74) & Chr(186) & Chr(114) & Chr(43) & Chr(147) & Chr(122) & Chr(146) & Chr(219) & Chr(226)
  loc_0040599B: var_36C = var_1EC & Chr(59) & Chr(226) & Chr(75) & Chr(251) & Chr(19) & Chr(123) & Chr(20) & Chr(92) & Chr(52) & Chr(235) & Chr(4) & Chr(20)
  loc_00405A67: var_4EC = var_36C & Chr(234) & Chr(195) & Chr(27) & Chr(28) & Chr(156) & Chr(68) & Chr(52) & Chr(116) & Chr(211) & Chr(67) & Chr(92) & Chr(44)
  loc_00405B33: var_66C = var_4EC & Chr(89) & Chr(132) & Chr(76) & Chr(131) & Chr(4) & Chr(100) & Chr(132) & Chr(121) & Chr(29) & Chr(69) & Chr(117) & Chr(21)
  loc_00405BFF: var_7EC = var_66C & Chr(4) & Chr(98) & Chr(66) & Chr(42) & Chr(82) & Chr(66) & Chr(98) & Chr(90) & Chr(114) & Chr(114) & Chr(130) & Chr(146)
  loc_00405C51: var_34 = var_7EC & Chr(146) & Chr(178) & Chr(162) & Chr(202)
End Sub

Public Sub Proc_0_13_406650
  Dim var_A8 As CommandButton
  loc_004066A7: On Error Resume Next
  loc_004066D4: FFFFFFFFh.Height = %x1s = FFFFFFFFh.Height = %x1s * eax+0000008Ch
  loc_004066DC: FFFFFFFFh.Height = %x1s = FFFFFFFFh.Height = %x1s - 0001h
  loc_004066E0: var_38 = FFFFFFFFh.Height = %x1s
  loc_004066EF: var_B8 = var_38
  loc_00406705: GoTo loc_00406716
  loc_00406707: 
  loc_0040670B: var_24 = var_24 + var_B4
  loc_00406712: var_24 = var_24+var_B4
  loc_00406716: 'Referenced from: 00406705
  loc_00406721: If var_24 <= var_38 Then
  loc_00406733:   If var_24 > 1 Then
  loc_00406777:     var_A8 = var_F0
  loc_004067B7:     var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_004067BC:     var_A4 = Unknown_VTable_Call[edx+00000040h]
  loc_004067FB:     var_E8 = var_54
  loc_00406829:     var_eax = Unknown_VTable_Call[ecx+0000000Ch]
  loc_0040682E:     var_AC = Unknown_VTable_Call[ecx+0000000Ch]
  loc_0040687D:   End If
  loc_004068BE:   var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_004068C3:   var_A4 = Unknown_VTable_Call[edx+00000040h]
  loc_00406902:   var_A8 = var_54
  loc_0040691C:   cmdButton.Caption = global_0040302C
  loc_00406921:   var_AC = var_A8
  loc_00406977:   GoTo loc_00406707
  loc_0040697C: End If
  loc_0040699C: var_C0 = Len(arg_C)
  loc_004069B2: GoTo loc_004069C3
  loc_004069B4: 
  loc_004069B8: var_24 = var_24 + var_BC
  loc_004069BF: var_24 = var_24+var_BC
  loc_004069C3: 'Referenced from: 004069B2
  loc_004069CE: If var_24 <= Len(arg_C) Then
  loc_004069EC:   var_80 = arg_C
  loc_00406A22:   var_28 = Mid(arg_C, var_24, 2)
  loc_00406A4C:   var_2C = CInt(var_A0)
  loc_00406A5C:   If var_2C >= 0 Then
  loc_00406A66:     If var_2C > FFFFFFFFh.Height <> %x1s Then GoTo loc_00406A94
  loc_00406A68:   End If
  loc_00406A8F:   GoTo loc_00406ECE
  loc_00406AA3:   If var_2C <= FFFFFFh Then
  loc_00406ACC:     GoTo loc_00406ECE
  loc_00406AD1:   End If
  loc_00406ADC:   var_30 = var_2C
  loc_00406AEB:   var_9C = var_2C
  loc_00406B02:   var_eax = FrmMain.cmdButton_Click
  loc_00406B08:   var_A0 = FrmMain.cmdButton_Click
  loc_00406B4B:   GoTo loc_004069B4
  loc_00406B50: End If
  loc_00406B68: var_C8 = var_38
  loc_00406B7E: GoTo loc_00406B8F
  loc_00406B80: 
  loc_00406B84: var_24 = var_24 + var_C4
  loc_00406B8B: var_24 = var_24+var_C4
  loc_00406B8F: 'Referenced from: 00406B7E
  loc_00406B9A: If var_24 <= var_38 Then
  loc_00406BE1:   var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_00406BE6:   var_A4 = Unknown_VTable_Call[edx+00000040h]
  loc_00406C3E:   var_4C = cmdButton.Caption
  loc_00406C43:   var_AC = var_4C
  loc_00406C96:   var_B0 = (var_4C = global_00403074)
  loc_00406CC2:   If var_B0 Then
  loc_00406CD1:   End If
  loc_00406CD8:   GoTo loc_00406B80
  loc_00406CDD: End If
  loc_00406CE9: If var_34 = var_FFFFFF Then
  loc_00406D0C:   var_48 = CInt(1)
  loc_00406D12:   GoTo loc_00406D3B
  loc_00406D14: End If
  loc_00406D3B: 'Referenced from: 00406D12
  loc_00406D46: var_D0 = var_38
  loc_00406D5C: GoTo loc_00406D6D
  loc_00406D5E: 
  loc_00406D62: var_24 = var_24 + var_CC
  loc_00406D69: var_24 = var_24+var_CC
  loc_00406D6D: 'Referenced from: 00406D5C
  loc_00406D78: If var_24 <= var_38 Then
  loc_00406DBC:   var_A8 = var_110
  loc_00406DFC:   var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_00406E01:   var_A4 = Unknown_VTable_Call[edx+00000040h]
  loc_00406E40:   var_EC = var_54
  loc_00406E6E:   var_eax = Unknown_VTable_Call[ecx+00000010h]
  loc_00406E73:   var_AC = Unknown_VTable_Call[ecx+00000010h]
  loc_00406EC9:   GoTo loc_00406D5E
  loc_00406ECE: End If
  loc_00406ED3: GoTo loc_00406F1C
  loc_00406EDD: If 0 And 4 Then
  loc_00406EE8: End If
  loc_00406F1B: Exit Sub
  loc_00406F1C: 'Referenced from: 00406ED3
End Sub

Public Sub Proc_0_14_406F60
  loc_00406FBD: var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_00406FEB: var_14 = cmdButton.Caption
  loc_00407014: esi = (var_14 = global_0040302C) + 1
  loc_00407036: If (var_14 = global_0040302C) + 1 Then
  loc_0040705E:   var_eax = Unknown_VTable_Call[edx+00000040h]
  loc_0040707F:   cmdButton.Caption = global_00403074
  loc_0040709B:   GoTo loc_00407100
  loc_0040709D: End If
  loc_004070C3: var_eax = Unknown_VTable_Call[eax+00000040h]
  loc_004070E4: cmdButton.Caption = global_0040302C
  loc_00407100: 'Referenced from: 0040709B
  loc_00407110: GoTo loc_0040712F
  loc_0040712E: Exit Sub
  loc_0040712F: 'Referenced from: 00407110
End Sub

Public Sub Proc_0_15_407150
  loc_004071A1: var_44 = arg_C
  loc_004071CD: var_24 = StrConv(arg_C, 128, 0)
  loc_004071E4: var_44 = %x1 = 0.Enabled
  loc_00407226: var_1C = Me.
  loc_00407237: var_44 = var_24
  loc_004072C7: var_20 = var_1C.encrypt(esi, var_58, 11)
  loc_004072CE: GoTo loc_004072FC
  loc_004072D4: If var_4 Then
  loc_004072E3:   GoTo loc_004072E7
  loc_004072E5: End If
  loc_004072E7: 'Referenced from: 004072E3
  loc_004072FB: Exit Sub
  loc_004072FC: 'Referenced from: 004072CE
End Sub

Public Sub Proc_0_16_407480
  loc_004074F5: If Len(arg_C) > 15 Then
  loc_00407513:   var_6C = arg_C
  loc_00407531:   arg_C = Mid(arg_C, 1, 15)
  loc_0040754A: End If
  loc_0040755F: var_9C = Len(arg_C)
  loc_00407570: If 00000001h <= Len(arg_C) Then
  loc_00407581:   var_6C = arg_C
  loc_004075BF:   var_24 = Asc(CStr(Mid(arg_C, 1, 1)))
  loc_004075E2:   If Not Sign(-2147483641 - 0) Then
  loc_004075E4:     eax = -2147483641 - 1
  loc_004075E8:     eax = -8 + 1
  loc_004075E9:   End If
  loc_004075ED:   08h = 08h - -8 + 1
  loc_004075EF:   var_2C = -8 + 1
  loc_004075FF:   var_7C = var_30
  loc_00407615:   var_88 = FrmMain.LShift(var_24, var_2C)
  loc_00407643:   var_8C = FrmMain.RShift(var_24, var_18)
  loc_00407671:   CheckObj(Me, global_00402858, 1784) And 255 = CheckObj(Me, global_00402858, 1784) And 255 + var_8C
  loc_0040767D:   var_3C = CheckObj(Me, global_00402858, 1784) And 255+var_8C xor ebx
  loc_00407687:   var_54 = Hex(CheckObj(Me, global_00402858, 1784) And 255+var_8C xor ebx)
  loc_004076AE:   var_30 = var_30 + Mid(arg_C, 1, 1)
  loc_004076C8:   Len(arg_C) xor 000000A5h = Len(arg_C) xor 000000A5h + 00000001h
  loc_004076D8:   00000001h = 00000001h + 00000001h
  loc_004076DA:   GoTo loc_0040756A
  loc_004076DF: End If
  loc_004076E5: var_20 = var_30
  loc_004076F0: GoTo loc_00407722
  loc_004076F6: If var_4 Then
  loc_00407701: End If
  loc_00407721: Exit Sub
  loc_00407722: 'Referenced from: 004076F0
End Sub

Public Sub Proc_0_17_407750
  loc_0040780A: Set var_58 = GetObject("winmgmts:\\.\root\cimv2", var_80)
  loc_0040784B: var_98 = "select * from win32_baseboard"
  loc_0040789B: For Each var_44 In Me.ExecQuery
  loc_004078A3:   If True Then
  loc_004078BC:     var_98 = var_48
  loc_004078ED:     var_48 =  & Me.product
  loc_00407922:   Next var_C4
  loc_00407928:   GoTo loc_004078A1
  loc_0040792D: End If
  loc_00407951: var_eax = FrmMain.Proc_0_16_407480(Me, var_48, var_5C, var_60)
  loc_0040795E: txtMachineCode.Text = var_5C
  loc_00407993: GoTo loc_004079D1
  loc_00407999: If var_4 Then
  loc_004079A4: End If
  loc_004079D0: Exit Sub
  loc_004079D1: 'Referenced from: 00407993
End Sub

Public Sub Proc_0_18_407C20
  loc_00407C83: var_58 = Len(arg_C)
  loc_00407C91: If 00000001h <= Len(arg_C) Then
  loc_00407CBB:   var_18 = Mid$(arg_C, 1, 1)
  loc_00407CCB:   call Like("[A-Za-z0-9]", var_18, 0, %ecx = %S_edx_S, undef 'Ignore this '__vbaFreeVar)
  loc_00407CD4:   If Like("[A-Za-z0-9]", var_18, 0, %ecx = %S_edx_S, undef 'Ignore this '__vbaFreeVar) = 0 Then
  loc_00407CEB:     If (var_18 = global_00403198) = 0 Then
  loc_00407CFB:       GoTo loc_00407D83
  loc_00407D00:     End If
  loc_00407D0E:     var_38 = Asc(var_18)
  loc_00407D61:     var_18 = global_004031A0 & Right$(global_00402FCC & Hex$(Asc(var_18)), 2)
  loc_00407D83:   End If
  loc_00407D92:   var_20 = var_20 & var_18
  loc_00407D9E:   var_1C = var_1C(1)
  loc_00407DA3:   GoTo loc_00407C8E
  loc_00407DA8: End If
  loc_00407DAD: GoTo loc_00407DE3
  loc_00407DB3: If var_4 Then
  loc_00407DBE: End If
  loc_00407DE2: Exit Sub
  loc_00407DE3: 'Referenced from: 00407DAD
End Sub
