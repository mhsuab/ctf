0000: pusha 0075
0003: pushw 0000 (\x00)
0005: pushw 000a (\n)
0007: pushw 003f (?)
0009: pushw 0065 (e)
000b: pushw 0076 (v)
000d: pushw 0069 (i)
000f: pushw 006c (l)
0011: pushw 0061 (a)
0013: pushw 0020 ( )
0015: pushw 0074 (t)
0017: pushw 0075 (u)
0019: pushw 006f (o)
001b: pushw 0020 ( )
001d: pushw 0074 (t)
001f: pushw 0069 (i)
0021: pushw 0020 ( )
0023: pushw 0065 (e)
0025: pushw 006b (k)
0027: pushw 0061 (a)
0029: pushw 006d (m)
002b: pushw 0020 ( )
002d: pushw 0075 (u)
002f: pushw 006f (o)
0031: pushw 0079 (y)
0033: pushw 0020 ( )
0035: pushw 006e (n)
0037: pushw 0061 (a)
0039: pushw 0043 (C)
003b: pushw 000a (\n)
003d: pushw 0058 (X)
003f: pushw 0020 ( )
0041: pushw 0049 (I)
0043: pushw 0020 ( )
0045: pushw 0052 (R)
0047: pushw 0020 ( )
0049: pushw 0054 (T)
004b: pushw 0020 ( )
004d: pushw 0041 (A)
004f: pushw 0020 ( )
0051: pushw 004d (M)
0053: pushw 0020 ( )
0055: pushw 0065 (e)
0057: pushw 0068 (h)
0059: pushw 0074 (t)
005b: pushw 0020 ( )
005d: pushw 006f (o)
005f: pushw 0074 (t)
0061: pushw 0020 ( )
0063: pushw 0065 (e)
0065: pushw 006d (m)
0067: pushw 006f (o)
0069: pushw 0063 (c)
006b: pushw 006c (l)
006d: pushw 0065 (e)
006f: pushw 0057 (W)
0071: pusha 013b<putc>
0074: jmp                       call <putc>
0075: pushw 0001 (\x01)         x = 1
0077: pushw 0001 (\x01)         y = 1
0079: pushw 0000 (\x00)         z = 1
007b: getc                      function <getc>
007c: copy
007d: pushw 0075 (u)
007f: sub
0080: pusha 00a0
0083: jz
0084: copy
0085: pushw 0064 (d)
0087: sub
0088: pusha 00aa
008b: jz
008c: copy
008d: pushw 006c (l)
008f: sub
0090: pusha 00b4
0093: jz
0094: copy
0095: pushw 0072 (r)
0097: sub
0098: pusha 00c0
009b: jz
009c: pusha 00fb<lose>          call <lose>
009f: jmp
00a0: pop                       case 'u'
00a1: store                     # store z
00a2: pushw 0001 (\x01)
00a4: sub                       # y -= 1
00a5: load                      # load z
00a6: pusha 00cc
00a9: jmp
00aa: pop                       case 'd'
00ab: store
00ac: pushw 0001 (\x01)
00ae: add
00af: load
00b0: pusha 00cc
00b3: jmp
00b4: pop                       case 'l'
00b5: store
00b6: store
00b7: pushw 0001 (\x01)
00b9: sub
00ba: load
00bb: load
00bc: pusha 00cc
00bf: jmp
00c0: pop                       case 'r'
00c1: store
00c2: store
00c3: pushw 0001 (\x01)
00c5: add
00c6: load
00c7: load
00c8: pusha 00cc
00cb: jmp
00cc: store                     store z; # after modifying x, y
00cd: store                     store y
00ce: pusha 00da                return address
00d1: load                      load y
00d2: copy                      stack: x-ret_addr-y-y, mem: z
00d3: store                     stack: x-ret_addr-y, mem: z-y
00d4: pushw 0010 (\x10)
00d6: pusha 0147<mul>
00d9: jmp                       call <mul>(0x10, y)
00da: swap
00db: copy
00dc: store
00dd: add
00de: load
00df: swap
00e0: load
00e1: swap
00e2: load
00e3: swap                      stack: x-y-z-(x + 0x10 * y)
00e4: store
00e5: pusha 00ef
00e8: load
00e9: pushw 0002 (\x02)
00eb: pusha 0161
00ee: jmp                       call <shift_left>(2, `x + 0x10 * y`) = `` <<2
00ef: pusha 007b<getc>
00f2: swap
00f3: pusha 0174<matrix_base>   0x174 + (result of <shift_left>)
00f6: add
00f7: jmp
00f8: pushw 0000 (\x00)             function <exit_0>
00fa: ret
00fb: pusha 0138                    function <lose>
00fe: pushw 0000 (\x00)
0100: pushw 000a (\n)
0102: pushw 002e (.)
0104: pushw 0065 (e)
0106: pushw 0075 (u)
0108: pushw 0072 (r)
010a: pushw 0067 (g)
010c: pushw 0020 ( )
010e: pushw 0061 (a)
0110: pushw 0020 ( )
0112: pushw 0079 (y)
0114: pushw 0062 (b)
0116: pushw 0020 ( )
0118: pushw 006e (n)
011a: pushw 0065 (e)
011c: pushw 0074 (t)
011e: pushw 0061 (a)
0120: pushw 0065 (e)
0122: pushw 0020 ( )
0124: pushw 0065 (e)
0126: pushw 0072 (r)
0128: pushw 0065 (e)
012a: pushw 0077 (w)
012c: pushw 0020 ( )
012e: pushw 0075 (u)
0130: pushw 006f (o)
0132: pushw 0059 (Y)
0134: pusha 013b<putc>
0137: jmp                       call <putc>
0138: pushw 0001 (\x01)
013a: ret
013b: copy                      function <putc>
013c: pusha 0145
013f: jz
0140: putc
0141: pusha 013b<putc>
0144: jmp
0145: pop
0146: jmp                       end <putc>
0147: pushw 0000 (\x00)         function <mul>, stack: x-ret_addr-y-0x10-0x0, mem: z-y
0149: store                     store 0x0 = v0 -> v0 + ? * a0
014a: store                     store 0x10 = a0-> a0
014b: copy                      stack: x-ret_addr-y-(y-1)
014c: pusha 015b
014f: jz
0150: pushw 0001 (\x01)
0152: sub                       ...-(y - 1) -> ...-(y-n)
0153: load                      ...-(y-n)-a0
0154: copy                      ...-(y-n)-a0-a0
0155: load                      ...-(y-n)-a0-a0-v0
0156: add                       ...-(y-n)-a0-(a0+v0)
0157: pusha 0149
015a: jmp
015b: pop                       ...-y-0-
015c: load
015d: pop
015e: load
015f: swap
0160: jmp                       end <mul>
0161: copy                      function <shift_left>(a, b) = (b << a)
0162: pusha 0171
0165: jz
0166: pushw 0001 (\x01)
0168: sub
0169: store
016a: copy
016b: add
016c: load
016d: pusha 0161
0170: jmp
0171: pop
0172: swap
0173: jmp                       end <shift_left>
0174: pusha 00fb<lose>          call <lose>     <- start of table
0177: jmp
0178: pusha 00fb<lose>          call <lose>
017b: jmp
017c: pusha 00fb<lose>          call <lose>
017f: jmp
0180: pusha 00fb<lose>          call <lose>
0183: jmp
0184: pusha 00fb<lose>          call <lose>
0187: jmp
0188: pusha 00fb<lose>          call <lose>
018b: jmp
018c: pusha 00fb<lose>          call <lose>
018f: jmp
0190: pusha 00fb<lose>          call <lose>
0193: jmp
0194: pusha 00fb<lose>          call <lose>
0197: jmp
0198: pusha 00fb<lose>          call <lose>
019b: jmp
019c: pusha 00fb<lose>          call <lose>
019f: jmp
01a0: pusha 00fb<lose>          call <lose>
01a3: jmp
01a4: pusha 00fb<lose>          call <lose>
01a7: jmp
01a8: pusha 00fb<lose>          call <lose>
01ab: jmp
01ac: pusha 00fb<lose>          call <lose>
01af: jmp
01b0: pusha 00fb<lose>          call <lose>
01b3: jmp
01b4: pusha 00fb<lose>          call <lose>
01b7: jmp
01b8: jmp
01b9: nop
01ba: nop
01bb: nop
01bc: jmp
01bd: nop
01be: nop
01bf: nop
01c0: jmp
01c1: nop
01c2: nop
01c3: nop
01c4: jmp
01c5: nop
01c6: nop
01c7: nop
01c8: jmp
01c9: nop
01ca: nop
01cb: nop
01cc: pusha 057f<add_z>
01cf: jmp
01d0: pusha 00fb<lose>          call <lose>
01d3: jmp
01d4: jmp
01d5: nop
01d6: nop
01d7: nop
01d8: pusha 00fb<lose>          call <lose>
01db: jmp
01dc: pusha 057f<add_z>
01df: jmp
01e0: jmp
01e1: nop
01e2: nop
01e3: nop
01e4: jmp
01e5: nop
01e6: nop
01e7: nop
01e8: pusha 00fb<lose>          call <lose>
01eb: jmp
01ec: jmp
01ed: nop
01ee: nop
01ef: nop
01f0: pusha 00fb<lose>          call <lose>
01f3: jmp
01f4: pusha 00fb<lose>          call <lose>
01f7: jmp
01f8: pusha 00fb<lose>          call <lose>
01fb: jmp
01fc: pusha 00fb<lose>          call <lose>
01ff: jmp
0200: pusha 00fb<lose>          call <lose>
0203: jmp
0204: pusha 0574<sub_z>
0207: jmp
0208: pusha 00fb<lose>          call <lose>
020b: jmp
020c: pusha 00fb<lose>          call <lose>
020f: jmp
0210: pusha 00fb<lose>          call <lose>
0213: jmp
0214: jmp
0215: nop
0216: nop
0217: nop
0218: pusha 00fb<lose>          call <lose>
021b: jmp
021c: pusha 00fb<lose>          call <lose>
021f: jmp
0220: pusha 00fb<lose>          call <lose>
0223: jmp
0224: jmp
0225: nop
0226: nop
0227: nop
0228: pusha 00fb<lose>          call <lose>
022b: jmp
022c: jmp
022d: nop
022e: nop
022f: nop
0230: pusha 00fb<lose>          call <lose>
0233: jmp
0234: pusha 00fb<lose>          call <lose>
0237: jmp
0238: jmp
0239: nop
023a: nop
023b: nop
023c: jmp
023d: nop
023e: nop
023f: nop
0240: jmp
0241: nop
0242: nop
0243: nop
0244: jmp
0245: nop
0246: nop
0247: nop
0248: jmp
0249: nop
024a: nop
024b: nop
024c: jmp
024d: nop
024e: nop
024f: nop
0250: jmp
0251: nop
0252: nop
0253: nop
0254: jmp
0255: nop
0256: nop
0257: nop
0258: jmp
0259: nop
025a: nop
025b: nop
025c: jmp
025d: nop
025e: nop
025f: nop
0260: pusha 00fb<lose>          call <lose>
0263: jmp
0264: jmp
0265: nop
0266: nop
0267: nop
0268: pusha 00fb<lose>          call <lose>
026b: jmp
026c: jmp
026d: nop
026e: nop
026f: nop
0270: pusha 00fb<lose>          call <lose>
0273: jmp
0274: pusha 00fb<lose>          call <lose>
0277: jmp
0278: pusha 00fb<lose>          call <lose>
027b: jmp
027c: jmp
027d: nop
027e: nop
027f: nop
0280: pusha 00fb<lose>          call <lose>
0283: jmp
0284: jmp
0285: nop
0286: nop
0287: nop
0288: pusha 00fb<lose>          call <lose>
028b: jmp
028c: pusha 00fb<lose>          call <lose>
028f: jmp
0290: pusha 00fb<lose>          call <lose>
0293: jmp
0294: pusha 00fb<lose>          call <lose>
0297: jmp
0298: pusha 00fb<lose>          call <lose>
029b: jmp
029c: jmp
029d: nop
029e: nop
029f: nop
02a0: pusha 00fb<lose>          call <lose>
02a3: jmp
02a4: jmp
02a5: nop
02a6: nop
02a7: nop
02a8: pusha 0574<sub_z>
02ab: jmp
02ac: jmp
02ad: nop
02ae: nop
02af: nop
02b0: pusha 00fb<lose>          call <lose>
02b3: jmp
02b4: pusha 00fb<lose>          call <lose>
02b7: jmp
02b8: jmp
02b9: nop
02ba: nop
02bb: nop
02bc: jmp
02bd: nop
02be: nop
02bf: nop
02c0: pusha 00fb<lose>          call <lose>
02c3: jmp
02c4: jmp
02c5: nop
02c6: nop
02c7: nop
02c8: pusha 00fb<lose>          call <lose>
02cb: jmp
02cc: pusha 057f<add_z>
02cf: jmp
02d0: jmp
02d1: nop
02d2: nop
02d3: nop
02d4: jmp
02d5: nop
02d6: nop
02d7: nop
02d8: pusha 00fb<lose>          call <lose>
02db: jmp
02dc: jmp
02dd: nop
02de: nop
02df: nop
02e0: pusha 00fb<lose>          call <lose>
02e3: jmp
02e4: jmp
02e5: nop
02e6: nop
02e7: nop
02e8: pusha 00fb<lose>          call <lose>
02eb: jmp
02ec: jmp
02ed: nop
02ee: nop
02ef: nop
02f0: pusha 00fb<lose>          call <lose>
02f3: jmp
02f4: pusha 00fb<lose>          call <lose>
02f7: jmp
02f8: jmp
02f9: nop
02fa: nop
02fb: nop
02fc: pusha 00fb<lose>          call <lose>
02ff: jmp
0300: pusha 00fb<lose>          call <lose>
0303: jmp
0304: jmp
0305: nop
0306: nop
0307: nop
0308: pusha 00fb<lose>          call <lose>
030b: jmp
030c: pusha 00fb<lose>          call <lose>
030f: jmp
0310: pusha 00fb<lose>          call <lose>
0313: jmp
0314: jmp
0315: nop
0316: nop
0317: nop
0318: pusha 00fb<lose>          call <lose>
031b: jmp
031c: jmp
031d: nop
031e: nop
031f: nop
0320: pusha 00fb<lose>          call <lose>
0323: jmp
0324: jmp
0325: nop
0326: nop
0327: nop
0328: pusha 00fb<lose>          call <lose>
032b: jmp
032c: jmp
032d: nop
032e: nop
032f: nop
0330: pusha 00fb<lose>          call <lose>
0333: jmp
0334: pusha 00fb<lose>          call <lose>
0337: jmp
0338: jmp
0339: nop
033a: nop
033b: nop
033c: pusha 00fb<lose>          call <lose>
033f: jmp
0340: jmp
0341: nop
0342: nop
0343: nop
0344: jmp
0345: nop
0346: nop
0347: nop
0348: jmp
0349: nop
034a: nop
034b: nop
034c: jmp
034d: nop
034e: nop
034f: nop
0350: jmp
0351: nop
0352: nop
0353: nop
0354: jmp
0355: nop
0356: nop
0357: nop
0358: pusha 00fb<lose>          call <lose>
035b: jmp
035c: jmp
035d: nop
035e: nop
035f: nop
0360: pusha 00fb<lose>          call <lose>
0363: jmp
0364: jmp
0365: nop
0366: nop
0367: nop
0368: pusha 00fb<lose>          call <lose>
036b: jmp
036c: jmp
036d: nop
036e: nop
036f: nop
0370: pusha 00fb<lose>          call <lose>
0373: jmp
0374: pusha 00fb<lose>          call <lose>
0377: jmp
0378: jmp
0379: nop
037a: nop
037b: nop
037c: pusha 00fb<lose>          call <lose>
037f: jmp
0380: jmp
0381: nop
0382: nop
0383: nop
0384: pusha 00fb<lose>          call <lose>
0387: jmp
0388: pusha 00fb<lose>          call <lose>
038b: jmp
038c: pusha 00fb<lose>          call <lose>
038f: jmp
0390: pusha 00fb<lose>          call <lose>
0393: jmp
0394: pusha 00fb<lose>          call <lose>
0397: jmp
0398: pusha 00fb<lose>          call <lose>
039b: jmp
039c: jmp
039d: nop
039e: nop
039f: nop
03a0: pusha 00fb<lose>          call <lose>
03a3: jmp
03a4: jmp
03a5: nop
03a6: nop
03a7: nop
03a8: pusha 00fb<lose>          call <lose>
03ab: jmp
03ac: jmp
03ad: nop
03ae: nop
03af: nop
03b0: pusha 00fb<lose>          call <lose>
03b3: jmp
03b4: pusha 00fb<lose>          call <lose>
03b7: jmp
03b8: jmp
03b9: nop
03ba: nop
03bb: nop
03bc: pusha 00fb<lose>          call <lose>
03bf: jmp
03c0: jmp
03c1: nop
03c2: nop
03c3: nop
03c4: jmp
03c5: nop
03c6: nop
03c7: nop
03c8: jmp
03c9: nop
03ca: nop
03cb: nop
03cc: jmp
03cd: nop
03ce: nop
03cf: nop
03d0: jmp
03d1: nop
03d2: nop
03d3: nop
03d4: jmp
03d5: nop
03d6: nop
03d7: nop
03d8: jmp
03d9: nop
03da: nop
03db: nop
03dc: jmp
03dd: nop
03de: nop
03df: nop
03e0: pusha 00fb<lose>          call <lose>
03e3: jmp
03e4: jmp
03e5: nop
03e6: nop
03e7: nop
03e8: pusha 00fb<lose>          call <lose>
03eb: jmp
03ec: jmp
03ed: nop
03ee: nop
03ef: nop
03f0: pusha 00fb<lose>          call <lose>
03f3: jmp
03f4: pusha 00fb<lose>          call <lose>
03f7: jmp
03f8: jmp
03f9: nop
03fa: nop
03fb: nop
03fc: pusha 00fb<lose>          call <lose>
03ff: jmp
0400: pusha 00fb<lose>          call <lose>
0403: jmp
0404: pusha 00fb<lose>          call <lose>
0407: jmp
0408: jmp
0409: nop
040a: nop
040b: nop
040c: pusha 00fb<lose>          call <lose>
040f: jmp
0410: pusha 00fb<lose>          call <lose>
0413: jmp
0414: pusha 00fb<lose>          call <lose>
0417: jmp
0418: pusha 00fb<lose>          call <lose>
041b: jmp
041c: pusha 00fb<lose>          call <lose>
041f: jmp
0420: pusha 00fb<lose>          call <lose>
0423: jmp
0424: jmp
0425: nop
0426: nop
0427: nop
0428: pusha 00fb<lose>          call <lose>
042b: jmp
042c: jmp
042d: nop
042e: nop
042f: nop
0430: pusha 00fb<lose>          call <lose>
0433: jmp
0434: pusha 00fb<lose>          call <lose>
0437: jmp
0438: jmp
0439: nop
043a: nop
043b: nop
043c: jmp
043d: nop
043e: nop
043f: nop
0440: jmp
0441: nop
0442: nop
0443: nop
0444: pusha 00fb<lose>          call <lose>
0447: jmp
0448: jmp
0449: nop
044a: nop
044b: nop
044c: jmp
044d: nop
044e: nop
044f: nop
0450: pusha 0574<sub_z>
0453: jmp
0454: jmp
0455: nop
0456: nop
0457: nop
0458: jmp
0459: nop
045a: nop
045b: nop
045c: pusha 00fb<lose>          call <lose>
045f: jmp
0460: jmp
0461: nop
0462: nop
0463: nop
0464: jmp
0465: nop
0466: nop
0467: nop
0468: pusha 00fb<lose>          call <lose>
046b: jmp
046c: jmp
046d: nop
046e: nop
046f: nop
0470: pusha 00fb<lose>          call <lose>
0473: jmp
0474: pusha 00fb<lose>          call <lose>
0477: jmp
0478: jmp
0479: nop
047a: nop
047b: nop
047c: pusha 00fb<lose>          call <lose>
047f: jmp
0480: pusha 00fb<lose>          call <lose>
0483: jmp
0484: pusha 00fb<lose>          call <lose>
0487: jmp
0488: jmp
0489: nop
048a: nop
048b: nop
048c: jmp
048d: nop
048e: nop
048f: nop
0490: pusha 00fb<lose>          call <lose>
0493: jmp
0494: jmp
0495: nop
0496: nop
0497: nop
0498: jmp
0499: nop
049a: nop
049b: nop
049c: pusha 00fb<lose>          call <lose>
049f: jmp
04a0: jmp
04a1: nop
04a2: nop
04a3: nop
04a4: pusha 00fb<lose>          call <lose>
04a7: jmp
04a8: jmp
04a9: nop
04aa: nop
04ab: nop
04ac: jmp
04ad: nop
04ae: nop
04af: nop
04b0: pusha 00fb<lose>          call <lose>
04b3: jmp
04b4: pusha 00fb<lose>          call <lose>
04b7: jmp
04b8: jmp
04b9: nop
04ba: nop
04bb: nop
04bc: pusha 00fb<lose>          call <lose>
04bf: jmp
04c0: jmp
04c1: nop
04c2: nop
04c3: nop
04c4: jmp
04c5: nop
04c6: nop
04c7: nop
04c8: jmp
04c9: nop
04ca: nop
04cb: nop
04cc: pusha 00fb<lose>          call <lose>
04cf: jmp
04d0: pusha 00fb<lose>          call <lose>
04d3: jmp
04d4: pusha 00fb<lose>          call <lose>
04d7: jmp
04d8: jmp
04d9: nop
04da: nop
04db: nop
04dc: pusha 00fb<lose>          call <lose>
04df: jmp
04e0: jmp
04e1: nop
04e2: nop
04e3: nop
04e4: pusha 00fb<lose>          call <lose>
04e7: jmp
04e8: pusha 0574<sub_z>
04eb: jmp
04ec: pusha 00fb<lose>          call <lose>
04ef: jmp
04f0: pusha 00fb<lose>          call <lose>
04f3: jmp
04f4: pusha 00fb<lose>          call <lose>
04f7: jmp
04f8: jmp
04f9: nop
04fa: nop
04fb: nop
04fc: pusha 00fb<lose>          call <lose>
04ff: jmp
0500: jmp
0501: nop
0502: nop
0503: nop
0504: jmp
0505: nop
0506: nop
0507: nop
0508: jmp
0509: nop
050a: nop
050b: nop
050c: jmp
050d: nop
050e: nop
050f: nop
0510: pusha 00fb<lose>          call <lose>
0513: jmp
0514: jmp
0515: nop
0516: nop
0517: nop
0518: jmp
0519: nop
051a: nop
051b: nop
051c: pusha 0574<sub_z>
051f: jmp
0520: jmp
0521: nop
0522: nop
0523: nop
0524: pusha 00fb<lose>          call <lose>
0527: jmp
0528: jmp
0529: nop
052a: nop
052b: nop
052c: jmp
052d: nop
052e: nop
052f: nop
0530: pusha 00fb<lose>          call <lose>
0533: jmp
0534: pusha 00fb<lose>          call <lose>
0537: jmp
0538: pusha 00fb<lose>          call <lose>
053b: jmp
053c: pusha 00fb<lose>          call <lose>
053f: jmp
0540: pusha 00fb<lose>          call <lose>
0543: jmp
0544: pusha 00fb<lose>          call <lose>
0547: jmp
0548: pusha 00fb<lose>          call <lose>
054b: jmp
054c: pusha 00fb<lose>          call <lose>
054f: jmp
0550: pusha 00fb<lose>          call <lose>
0553: jmp
0554: pusha 00fb<lose>          call <lose>
0557: jmp
0558: pusha 00fb<lose>          call <lose>
055b: jmp
055c: pusha 00fb<lose>          call <lose>
055f: jmp
0560: pusha 00fb<lose>          call <lose>
0563: jmp
0564: pusha 00fb<lose>          call <lose>
0567: jmp
0568: pusha 00fb<lose>          call <lose>
056b: jmp
056c: pusha 0585<win>           call <win>
056f: jmp
0570: pusha 00fb<lose>          call <lose>
0573: jmp
0574: store                     function<sub_z>
0575: copy
0576: pusha 00fb<lose>          if z == 0: call <lose>
0579: jz
057a: pushw 0001 (\x01)
057c: sub
057d: load
057e: jmp                       jmp back to <getc>
057f: store                     function<add_z>
0580: pushw 0001 (\x01)
0582: add
0583: load
0584: jmp                       jmp back to <getc>
0585: pop                       function <win>
0586: pop
0587: pop
0588: pop
0589: pusha 05ce
058c: pushw 0000 (\x00)
058e: pushw 000a (\n)
0590: pushw 0021 (!)
0592: pushw 0074 (t)
0594: pushw 0069 (i)
0596: pushw 0020 ( )
0598: pushw 0065 (e)
059a: pushw 0064 (d)
059c: pushw 0061 (a)
059e: pushw 006d (m)
05a0: pushw 0020 ( )
05a2: pushw 0075 (u)
05a4: pushw 006f (o)
05a6: pushw 0079 (y)
05a8: pushw 0020 ( )
05aa: pushw 002c (,)
05ac: pushw 0073 (s)
05ae: pushw 006e (n)
05b0: pushw 006f (o)
05b2: pushw 0069 (i)
05b4: pushw 0074 (t)
05b6: pushw 0061 (a)
05b8: pushw 006c (l)
05ba: pushw 0075 (u)
05bc: pushw 0074 (t)
05be: pushw 0061 (a)
05c0: pushw 0072 (r)
05c2: pushw 0067 (g)
05c4: pushw 006e (n)
05c6: pushw 006f (o)
05c8: pushw 0043 (C)
05ca: pusha 013b<putc>
05cd: jmp
05ce: pusha 00f8<exit_0>
05d1: jmp