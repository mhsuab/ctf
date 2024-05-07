using System;
using System.Diagnostics;
using System.Runtime.CompilerServices;
using FSharp.Json;
using MBrace.FsPickler;
using MBrace.FsPickler.Json;
using Microsoft.FSharp.Collections;
using Microsoft.FSharp.Core;

namespace <StartupCode$npcua-nautilus>
{
	// Token: 0x0200001D RID: 29
	internal static class $NPCUA
	{
		// Token: 0x060000FC RID: 252 RVA: 0x0000566C File Offset: 0x0000386C
		public static void main@()
		{
			$NPCUA._JsonConfig@12 = JsonConfig.create(FSharpOption<bool>.Some(true), null, null, null, FSharpOption<bool>.Some(true), null);
			$NPCUA.indent@1 = FSharpOption<bool>.Some(false);
			$NPCUA.omitHeader@1 = FSharpOption<bool>.Some(true);
			$NPCUA.typeConverter@1 = null;
			$NPCUA.picklerResolver@1 = null;
			$NPCUA._JsonSerializer@13 = new JsonSerializer(NPCUA.indent@1, NPCUA.omitHeader@1, NPCUA.typeConverter@1, NPCUA.picklerResolver@1);
			$NPCUA.log_level@15 = 0;
			NPCUA.VariableNode.Variables = MapModule.Empty<string, NPCUA.VariableNode>();
			NPCUA.VariableNode.init@58-1 = 3;
			$NPCUA.arg@1 = new NPCUA.VariableNode("/version", "npc://System/Environment/Version");
			$NPCUA.arg@1-1 = new NPCUA.VariableNode("/environment", "production");
			$NPCUA.application_pubkey@417 = null;
			$NPCUA.error_map@443 = MapModule.Empty<int, string>();
			NPCUA.error_map = NPCUA.error_map.Add(-2147418112, "Unknown error");
			$NPCUA.arg@1-2 = NPCUA.start_app();
		}

		// Token: 0x04000046 RID: 70
		[DebuggerBrowsable(0)]
		internal static JsonConfig _JsonConfig@12;

		// Token: 0x04000047 RID: 71
		[DebuggerBrowsable(0)]
		internal static JsonSerializer _JsonSerializer@13;

		// Token: 0x04000048 RID: 72
		[DebuggerBrowsable(0)]
		internal static FSharpOption<bool> indent@1;

		// Token: 0x04000049 RID: 73
		[DebuggerBrowsable(0)]
		internal static FSharpOption<bool> omitHeader@1;

		// Token: 0x0400004A RID: 74
		[DebuggerBrowsable(0)]
		internal static FSharpOption<ITypeNameConverter> typeConverter@1;

		// Token: 0x0400004B RID: 75
		[DebuggerBrowsable(0)]
		internal static FSharpOption<IPicklerResolver> picklerResolver@1;

		// Token: 0x0400004C RID: 76
		[DebuggerBrowsable(0)]
		internal static int log_level@15;

		// Token: 0x0400004D RID: 77
		[DebuggerBrowsable(0)]
		internal static NPCUA.VariableNode arg@1;

		// Token: 0x0400004E RID: 78
		[DebuggerBrowsable(0)]
		internal static NPCUA.VariableNode arg@1-1;

		// Token: 0x0400004F RID: 79
		[DebuggerBrowsable(0)]
		internal static byte[] application_pubkey@417;

		// Token: 0x04000050 RID: 80
		[DebuggerBrowsable(0)]
		internal static FSharpMap<int, string> error_map@443;

		// Token: 0x04000051 RID: 81
		[DebuggerBrowsable(0)]
		internal static int arg@1-2;

		// Token: 0x04000052 RID: 82
		[DebuggerBrowsable(0)]
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal static int init@;
	}
}
