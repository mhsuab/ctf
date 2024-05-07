using System;
using System.Collections;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using <StartupCode$npcua-nautilus>;
using crypto.nautilus;
using FSharp.Json;
using MBrace.FsPickler;
using MBrace.FsPickler.Json;
using Microsoft.FSharp.Collections;
using Microsoft.FSharp.Core;

// Token: 0x02000002 RID: 2
[CompilationMapping(7)]
public static class NPCUA
{
	// Token: 0x17000001 RID: 1
	// (get) Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
	[CompilationMapping(9)]
	public static JsonConfig _JsonConfig
	{
		get
		{
			return $NPCUA._JsonConfig@12;
		}
	}

	// Token: 0x17000002 RID: 2
	// (get) Token: 0x06000002 RID: 2 RVA: 0x00002058 File Offset: 0x00000258
	[CompilationMapping(9)]
	public static JsonSerializer _JsonSerializer
	{
		get
		{
			return $NPCUA._JsonSerializer@13;
		}
	}

	// Token: 0x17000003 RID: 3
	// (get) Token: 0x06000003 RID: 3 RVA: 0x00002060 File Offset: 0x00000260
	[CompilationMapping(9)]
	internal static FSharpOption<bool> indent@1
	{
		get
		{
			return $NPCUA.indent@1;
		}
	}

	// Token: 0x17000004 RID: 4
	// (get) Token: 0x06000004 RID: 4 RVA: 0x00002068 File Offset: 0x00000268
	[CompilationMapping(9)]
	internal static FSharpOption<bool> omitHeader@1
	{
		get
		{
			return $NPCUA.omitHeader@1;
		}
	}

	// Token: 0x17000005 RID: 5
	// (get) Token: 0x06000005 RID: 5 RVA: 0x00002070 File Offset: 0x00000270
	[CompilationMapping(9)]
	internal static FSharpOption<ITypeNameConverter> typeConverter@1
	{
		get
		{
			return $NPCUA.typeConverter@1;
		}
	}

	// Token: 0x17000006 RID: 6
	// (get) Token: 0x06000006 RID: 6 RVA: 0x00002078 File Offset: 0x00000278
	[CompilationMapping(9)]
	internal static FSharpOption<IPicklerResolver> picklerResolver@1
	{
		get
		{
			return $NPCUA.picklerResolver@1;
		}
	}

	// Token: 0x17000007 RID: 7
	// (get) Token: 0x06000007 RID: 7 RVA: 0x00002080 File Offset: 0x00000280
	// (set) Token: 0x06000008 RID: 8 RVA: 0x00002088 File Offset: 0x00000288
	[CompilationMapping(9)]
	public static int log_level
	{
		get
		{
			return $NPCUA.log_level@15;
		}
		set
		{
			$NPCUA.log_level@15 = value;
		}
	}

	// Token: 0x06000009 RID: 9 RVA: 0x00002090 File Offset: 0x00000290
	public static void writeToStderr(string s)
	{
		Console.Error.WriteLine(s);
	}

	// Token: 0x0600000A RID: 10 RVA: 0x000020A0 File Offset: 0x000002A0
	public static void dontWrite(string s)
	{
	}

	// Token: 0x0600000B RID: 11 RVA: 0x000020A4 File Offset: 0x000002A4
	[CompilationArgumentCounts(new int[]
	{
		1,
		1
	})]
	public static void debug_printfn<a, b>(a format, params b arr)
	{
	}

	// Token: 0x17000008 RID: 8
	// (get) Token: 0x0600000C RID: 12 RVA: 0x000020A8 File Offset: 0x000002A8
	[CompilationMapping(9)]
	internal static global::NPCUA.VariableNode arg@1
	{
		get
		{
			return $NPCUA.arg@1;
		}
	}

	// Token: 0x17000009 RID: 9
	// (get) Token: 0x0600000D RID: 13 RVA: 0x000020B0 File Offset: 0x000002B0
	[CompilationMapping(9)]
	internal static global::NPCUA.VariableNode arg@1-1
	{
		get
		{
			return $NPCUA.arg@1-1;
		}
	}

	// Token: 0x0600000E RID: 14 RVA: 0x000020B8 File Offset: 0x000002B8
	public static FSharpMap<string, Tuple<int, string>> loadStatusCodes(string fileName)
	{
		FSharpMap<string, Tuple<int, string>> result;
		using (StreamReader streamReader = new StreamReader(fileName))
		{
			FSharpMap<string, Tuple<int, string>> fsharpMap = MapModule.Empty<string, Tuple<int, string>>();
			while (!streamReader.EndOfStream)
			{
				string text = streamReader.ReadLine();
				string[] array = text.Split(',', StringSplitOptions.None);
				string text2 = array[0];
				int item = LanguagePrimitives.ParseInt32(array[1]);
				string text3 = array[2];
				string item2 = text3.Substring(1, text3.Length - 2);
				fsharpMap = fsharpMap.Add(text2, new Tuple<int, string>(item, item2));
			}
			result = fsharpMap;
		}
		return result;
	}

	// Token: 0x0600000F RID: 15 RVA: 0x00002168 File Offset: 0x00000368
	[CompilationArgumentCounts(new int[]
	{
		1,
		1
	})]
	public static FSharpOption<T> tryFindMapValueAsType<T>(FSharpMap<string, object> map, string key)
	{
		FSharpOption<object> fsharpOption = map.TryFind(key);
		if (fsharpOption == null)
		{
			return null;
		}
		FSharpOption<object> fsharpOption2 = fsharpOption;
		object value = fsharpOption2.Value;
		return FSharpOption<T>.Some(LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<T>(value));
	}

	// Token: 0x06000010 RID: 16 RVA: 0x00002198 File Offset: 0x00000398
	public static FSharpOption<int> int32Option(FSharpOption<decimal> d)
	{
		if (d == null)
		{
			return null;
		}
		decimal value = d.Value;
		return FSharpOption<int>.Some((int)value);
	}

	// Token: 0x06000011 RID: 17 RVA: 0x000021C4 File Offset: 0x000003C4
	public static FSharpOption<long> int64Option(FSharpOption<decimal> d)
	{
		if (d == null)
		{
			return null;
		}
		decimal value = d.Value;
		return FSharpOption<long>.Some((long)value);
	}

	// Token: 0x06000012 RID: 18 RVA: 0x000021F0 File Offset: 0x000003F0
	[CompilationArgumentCounts(new int[]
	{
		1,
		1,
		1
	})]
	public static T tryFindMapValueAsTypeDefault<T>(FSharpMap<string, object> map, string key, T def)
	{
		FSharpOption<object> fsharpOption = map.TryFind(key);
		if (fsharpOption == null)
		{
			return def;
		}
		FSharpOption<object> fsharpOption2 = fsharpOption;
		return LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<T>(fsharpOption2.Value);
	}

	// Token: 0x06000013 RID: 19 RVA: 0x0000221C File Offset: 0x0000041C
	[CompilerGenerated]
	internal static int CompareTo$cont@346(global::NPCUA.RequestHeader @this, global::NPCUA.RequestHeader obj, Unit unitVar)
	{
		IComparer genericComparer = LanguagePrimitives.GenericComparer;
		long timestamp@ = @this.timestamp@;
		long timestamp@2 = obj.timestamp@;
		int num = ((timestamp@ > timestamp@2) - (timestamp@ < timestamp@2)) ? 1 : 0;
		if (num < 0)
		{
			return num;
		}
		if (num > 0)
		{
			return num;
		}
		genericComparer = LanguagePrimitives.GenericComparer;
		int num2 = @this.requestHandle@;
		int num3 = obj.requestHandle@;
		int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
		if (num4 < 0)
		{
			return num4;
		}
		if (num4 > 0)
		{
			return num4;
		}
		num2 = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<int>>(LanguagePrimitives.GenericComparer, @this.returnDiagnostics@, obj.returnDiagnostics@);
		if (num2 < 0)
		{
			return num2;
		}
		if (num2 > 0)
		{
			return num2;
		}
		num3 = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(LanguagePrimitives.GenericComparer, @this.auditEntryId@, obj.auditEntryId@);
		if (num3 < 0)
		{
			return num3;
		}
		if (num3 > 0)
		{
			return num3;
		}
		return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<int>>(LanguagePrimitives.GenericComparer, @this.timeoutHint@, obj.timeoutHint@);
	}

	// Token: 0x06000014 RID: 20 RVA: 0x000022F0 File Offset: 0x000004F0
	[CompilerGenerated]
	internal static int CompareTo$cont@346-1(IComparer comp, global::NPCUA.RequestHeader @this, global::NPCUA.RequestHeader objTemp, Unit unitVar)
	{
		long timestamp@ = @this.timestamp@;
		long timestamp@2 = objTemp.timestamp@;
		int num = ((timestamp@ > timestamp@2) - (timestamp@ < timestamp@2)) ? 1 : 0;
		if (num < 0)
		{
			return num;
		}
		if (num > 0)
		{
			return num;
		}
		int num2 = @this.requestHandle@;
		int num3 = objTemp.requestHandle@;
		int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
		if (num4 < 0)
		{
			return num4;
		}
		if (num4 > 0)
		{
			return num4;
		}
		num2 = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<int>>(comp, @this.returnDiagnostics@, objTemp.returnDiagnostics@);
		if (num2 < 0)
		{
			return num2;
		}
		if (num2 > 0)
		{
			return num2;
		}
		num3 = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(comp, @this.auditEntryId@, objTemp.auditEntryId@);
		if (num3 < 0)
		{
			return num3;
		}
		if (num3 > 0)
		{
			return num3;
		}
		return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<int>>(comp, @this.timeoutHint@, objTemp.timeoutHint@);
	}

	// Token: 0x06000015 RID: 21 RVA: 0x000023A8 File Offset: 0x000005A8
	[CompilerGenerated]
	internal static int GetHashCode$cont@395(IEqualityComparer comp, global::NPCUA.DataValue @this, Unit unitVar)
	{
		int num = 0;
		num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<string>>(comp, @this.error@) + ((num << 6) + (num >> 2)));
		num = -1640531527 + (@this.serverPicoseconds@ + ((num << 6) + (num >> 2)));
		int num2 = -1640531527;
		long num3 = @this.serverTimestamp@;
		num = num2 + (((int)num3 ^ (int)(num3 >> 32)) + ((num << 6) + (num >> 2)));
		num = -1640531527 + (@this.sourcePicoseconds@ + ((num << 6) + (num >> 2)));
		int num4 = -1640531527;
		num3 = @this.sourceTimestamp@;
		num = num4 + (((int)num3 ^ (int)(num3 >> 32)) + ((num << 6) + (num >> 2)));
		num = (int)(2654435769U + (@this.statusCode@ + (uint)((num << 6) + (num >> 2))));
		return -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<object>>(comp, @this.value@) + ((num << 6) + (num >> 2)));
	}

	// Token: 0x1700000A RID: 10
	// (get) Token: 0x06000016 RID: 22 RVA: 0x0000246C File Offset: 0x0000066C
	// (set) Token: 0x06000017 RID: 23 RVA: 0x00002474 File Offset: 0x00000674
	[CompilationMapping(9)]
	public static byte[] application_pubkey
	{
		get
		{
			return $NPCUA.application_pubkey@417;
		}
		set
		{
			$NPCUA.application_pubkey@417 = value;
		}
	}

	// Token: 0x1700000B RID: 11
	// (get) Token: 0x06000018 RID: 24 RVA: 0x0000247C File Offset: 0x0000067C
	public static string pubkey_path
	{
		[CompilerGenerated]
		[DebuggerNonUserCode]
		get
		{
			return "public.ec.pem";
		}
	}

	// Token: 0x06000019 RID: 25 RVA: 0x00002484 File Offset: 0x00000684
	public static global::NPCUA.CryptoSystem GetCryptoSystem(string key_path)
	{
		string pub_key_path = key_path + "/" + "public.ec.pem";
		string priv_key_path = key_path + "/" + "private.ec.pem";
		FSharpFunc<Unit, Unit> loadPublicKey = new global::NPCUA.loadPublicKey@435(pub_key_path);
		FSharpFunc<Unit, Crypto> loadPrivateKey = new global::NPCUA.loadPrivateKey@437(priv_key_path);
		return new global::NPCUA.CryptoSystem(loadPublicKey, loadPrivateKey);
	}

	// Token: 0x1700000C RID: 12
	// (get) Token: 0x0600001A RID: 26 RVA: 0x000024C8 File Offset: 0x000006C8
	// (set) Token: 0x0600001B RID: 27 RVA: 0x000024D0 File Offset: 0x000006D0
	[CompilationMapping(9)]
	public static FSharpMap<int, string> error_map
	{
		get
		{
			return $NPCUA.error_map@443;
		}
		set
		{
			$NPCUA.error_map@443 = value;
		}
	}

	// Token: 0x0600001C RID: 28 RVA: 0x000024D8 File Offset: 0x000006D8
	internal static global::NPCUA.StatusCode make_res@667(global::NPCUA.NPCUA @this, string n)
	{
		return new global::NPCUA.StatusCode((uint)MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item1, (!string.Equals(n, "Good")) ? FSharpOption<string>.Some(MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item2) : null);
	}

	// Token: 0x0600001D RID: 29 RVA: 0x00002524 File Offset: 0x00000724
	internal static global::NPCUA.DataValue make_res@718-1(global::NPCUA.NPCUA @this, string n, FSharpOption<object> tupledArg1)
	{
		return new global::NPCUA.DataValue(tupledArg1, (uint)MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item1, 0L, 0, 0L, 0, (!string.Equals(n, "Good")) ? FSharpOption<string>.Some(MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item2) : null);
	}

	// Token: 0x0600001E RID: 30 RVA: 0x00002578 File Offset: 0x00000778
	internal static global::NPCUA.StatusCode make_res@785-2<a>(global::NPCUA.NPCUA @this, string n, a tupledArg1)
	{
		return new global::NPCUA.StatusCode((uint)MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item1, (!string.Equals(n, "Good")) ? FSharpOption<string>.Some(MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item2) : null);
	}

	// Token: 0x0600001F RID: 31 RVA: 0x000025C4 File Offset: 0x000007C4
	[CompilerGenerated]
	internal static bool contains@1<a>(a e, FSharpList<a> xs1)
	{
		while (xs1.TailOrNull != null)
		{
			FSharpList<a> fsharpList = xs1;
			FSharpList<a> tailOrNull = fsharpList.TailOrNull;
			a headOrDefault = fsharpList.HeadOrDefault;
			if (LanguagePrimitives.HashCompare.GenericEqualityIntrinsic<a>(e, headOrDefault))
			{
				return true;
			}
			a a = e;
			xs1 = tailOrNull;
			e = a;
		}
		return false;
	}

	// Token: 0x06000020 RID: 32 RVA: 0x00002600 File Offset: 0x00000800
	internal static global::NPCUA.DataValue make_res@863-3(global::NPCUA.NPCUA @this, string n, FSharpOption<object> tupledArg1)
	{
		return new global::NPCUA.DataValue(tupledArg1, (uint)MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item1, 0L, 0, 0L, 0, (!string.Equals(n, "Good")) ? FSharpOption<string>.Some(MapModule.Find<string, Tuple<int, string>>(n, @this.status_codes).Item2) : null);
	}

	// Token: 0x06000021 RID: 33 RVA: 0x00002654 File Offset: 0x00000854
	[CompilerGenerated]
	internal static bool contains@1-1<a>(a e, FSharpList<a> xs1)
	{
		while (xs1.TailOrNull != null)
		{
			FSharpList<a> fsharpList = xs1;
			FSharpList<a> tailOrNull = fsharpList.TailOrNull;
			a headOrDefault = fsharpList.HeadOrDefault;
			if (LanguagePrimitives.HashCompare.GenericEqualityIntrinsic<a>(e, headOrDefault))
			{
				return true;
			}
			a a = e;
			xs1 = tailOrNull;
			e = a;
		}
		return false;
	}

	// Token: 0x06000022 RID: 34 RVA: 0x00002690 File Offset: 0x00000890
	public static int start_app()
	{
		Stream inputIn = Console.OpenStandardInput();
		Stream outputIn = Console.OpenStandardOutput();
		global::NPCUA.NPCUA npcua = new global::NPCUA.NPCUA(inputIn, outputIn);
		for (;;)
		{
			npcua.read_msg();
		}
		return 1;
	}

	// Token: 0x1700000D RID: 13
	// (get) Token: 0x06000023 RID: 35 RVA: 0x000026C0 File Offset: 0x000008C0
	[CompilationMapping(9)]
	internal static int arg@1-2
	{
		get
		{
			return $NPCUA.arg@1-2;
		}
	}

	// Token: 0x02000003 RID: 3
	[CompilationMapping(3)]
	[Serializable]
	public enum AttributeId
	{
		// Token: 0x04000002 RID: 2
		NodeId = 1,
		// Token: 0x04000003 RID: 3
		NodeClass,
		// Token: 0x04000004 RID: 4
		DisplayName = 4,
		// Token: 0x04000005 RID: 5
		Description,
		// Token: 0x04000006 RID: 6
		Value = 13
	}

	// Token: 0x02000004 RID: 4
	[CompilationMapping(3)]
	[Serializable]
	public class Node
	{
		// Token: 0x06000024 RID: 36 RVA: 0x000026C8 File Offset: 0x000008C8
		public Node() : this()
		{
		}

		// Token: 0x06000025 RID: 37 RVA: 0x000026D4 File Offset: 0x000008D4
		public static bool Known(Uri target)
		{
			return false;
		}

		// Token: 0x06000026 RID: 38 RVA: 0x000026D8 File Offset: 0x000008D8
		public virtual string Serialize()
		{
			return global::NPCUA._JsonSerializer.PickleToString<object>(this, null, null);
		}

		// Token: 0x1700000E RID: 14
		// (get) Token: 0x06000027 RID: 39 RVA: 0x000026EC File Offset: 0x000008EC
		public virtual FSharpList<global::NPCUA.AttributeId> Allowed_attributes
		{
			get
			{
				return FSharpList<global::NPCUA.AttributeId>.Empty;
			}
		}

		// Token: 0x06000028 RID: 40 RVA: 0x000026F4 File Offset: 0x000008F4
		public virtual FSharpOption<object> Read_attribute(global::NPCUA.AttributeId aid)
		{
			return null;
		}

		// Token: 0x06000029 RID: 41 RVA: 0x000026F8 File Offset: 0x000008F8
		public virtual bool Write_attribute(global::NPCUA.AttributeId aid, object v)
		{
			return false;
		}
	}

	// Token: 0x02000005 RID: 5
	[CompilationMapping(3)]
	[Serializable]
	public class VariableNode : global::NPCUA.Node
	{
		// Token: 0x0600002A RID: 42 RVA: 0x000026FC File Offset: 0x000008FC
		public VariableNode(string name, object init_val)
		{
			FSharpRef<global::NPCUA.VariableNode> fsharpRef = new FSharpRef<global::NPCUA.VariableNode>(null);
			this..ctor();
			this.name@58 = name;
			fsharpRef.contents = this;
			this.variable = init_val;
			this.init@58 = 1;
			LanguagePrimitives.IntrinsicFunctions.CheckThis<global::NPCUA.VariableNode>(fsharpRef.contents).Install();
		}

		// Token: 0x1700000F RID: 15
		// (get) Token: 0x0600002B RID: 43 RVA: 0x00002748 File Offset: 0x00000948
		public string name
		{
			get
			{
				if (this.init@58 < 1)
				{
					LanguagePrimitives.IntrinsicFunctions.FailInit();
				}
				return this.name@58;
			}
		}

		// Token: 0x0600002C RID: 44 RVA: 0x00002768 File Offset: 0x00000968
		public void Install()
		{
			if (this.init@58 < 1)
			{
				LanguagePrimitives.IntrinsicFunctions.FailInit();
			}
			if (global::NPCUA.VariableNode.init@58-1 < 3)
			{
				LanguagePrimitives.IntrinsicFunctions.FailStaticInit();
			}
			if (global::NPCUA.VariableNode.init@58-1 < 3)
			{
				LanguagePrimitives.IntrinsicFunctions.FailStaticInit();
			}
			global::NPCUA.VariableNode.Variables = global::NPCUA.VariableNode.Variables.Add(this.name@58, this);
		}

		// Token: 0x0600002D RID: 45 RVA: 0x000027CC File Offset: 0x000009CC
		public override string Serialize()
		{
			if (this.init@58 < 1)
			{
				LanguagePrimitives.IntrinsicFunctions.FailInit();
			}
			string name = this.name;
			object obj = this.variable;
			FSharpFunc<Unit, global::NPCUA.VariableNode> fsharpFunc = new global::NPCUA.importVariableNode@76(name, obj);
			return global::NPCUA._JsonSerializer.PickleToString<object>(fsharpFunc, null, null);
		}

		// Token: 0x0600002E RID: 46 RVA: 0x00002814 File Offset: 0x00000A14
		public static FSharpOption<global::NPCUA.Node> Find(Uri target)
		{
			string absolutePath = target.AbsolutePath;
			if (global::NPCUA.VariableNode.init@58-1 < 3)
			{
				LanguagePrimitives.IntrinsicFunctions.FailStaticInit();
			}
			FSharpOption<global::NPCUA.VariableNode> fsharpOption = global::NPCUA.VariableNode.Variables.TryFind(absolutePath);
			if (fsharpOption != null)
			{
				return FSharpOption<global::NPCUA.Node>.Some(fsharpOption.Value);
			}
			return null;
		}

		// Token: 0x17000010 RID: 16
		// (get) Token: 0x0600002F RID: 47 RVA: 0x0000285C File Offset: 0x00000A5C
		public override FSharpList<global::NPCUA.AttributeId> Allowed_attributes
		{
			get
			{
				if (this.init@58 < 1)
				{
					LanguagePrimitives.IntrinsicFunctions.FailInit();
				}
				return FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.NodeId, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.NodeClass, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.DisplayName, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.Description, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.Value, FSharpList<global::NPCUA.AttributeId>.Empty)))));
			}
		}

		// Token: 0x06000030 RID: 48 RVA: 0x00002898 File Offset: 0x00000A98
		public override FSharpOption<object> Read_attribute(global::NPCUA.AttributeId aid)
		{
			if (this.init@58 < 1)
			{
				LanguagePrimitives.IntrinsicFunctions.FailInit();
			}
			if (aid == global::NPCUA.AttributeId.NodeId)
			{
				return FSharpOption<object>.Some("npc://Variable" + this.name);
			}
			if (aid == global::NPCUA.AttributeId.DisplayName)
			{
				return FSharpOption<object>.Some(this.name);
			}
			if (aid == global::NPCUA.AttributeId.Value)
			{
				return FSharpOption<object>.Some(this.variable);
			}
			return null;
		}

		// Token: 0x06000031 RID: 49 RVA: 0x000028FC File Offset: 0x00000AFC
		public override bool Write_attribute(global::NPCUA.AttributeId aid, object v)
		{
			if (this.init@58 < 1)
			{
				LanguagePrimitives.IntrinsicFunctions.FailInit();
			}
			this.variable = v;
			return true;
		}

		// Token: 0x06000032 RID: 50 RVA: 0x0000291C File Offset: 0x00000B1C
		static VariableNode()
		{
			$NPCUA.init@ = 0;
			int init@ = $NPCUA.init@;
		}

		// Token: 0x04000007 RID: 7
		internal string name@58;

		// Token: 0x04000008 RID: 8
		internal static FSharpMap<string, global::NPCUA.VariableNode> Variables;

		// Token: 0x04000009 RID: 9
		internal object variable;

		// Token: 0x0400000A RID: 10
		internal static int init@58-1;

		// Token: 0x0400000B RID: 11
		internal int init@58;
	}

	// Token: 0x02000006 RID: 6
	[Serializable]
	internal sealed class importVariableNode@76 : FSharpFunc<Unit, global::NPCUA.VariableNode>
	{
		// Token: 0x06000033 RID: 51 RVA: 0x0000292C File Offset: 0x00000B2C
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal importVariableNode@76(string _name, object _variable)
		{
			this._name = _name;
			this._variable = _variable;
		}

		// Token: 0x06000034 RID: 52 RVA: 0x00002944 File Offset: 0x00000B44
		public override global::NPCUA.VariableNode Invoke(Unit unitVar0)
		{
			return new global::NPCUA.VariableNode(this._name, this._variable);
		}

		// Token: 0x0400000C RID: 12
		public string _name;

		// Token: 0x0400000D RID: 13
		public object _variable;
	}

	// Token: 0x02000007 RID: 7
	[CompilationMapping(3)]
	[Serializable]
	public class SystemNode : global::NPCUA.Node
	{
		// Token: 0x06000035 RID: 53 RVA: 0x00002958 File Offset: 0x00000B58
		public SystemNode(string path) : this()
		{
			this.path@115 = path;
		}

		// Token: 0x06000036 RID: 54 RVA: 0x0000296C File Offset: 0x00000B6C
		public static string GetSystemProperty(string path)
		{
			string[] array = path.Split("/", StringSplitOptions.None);
			string text = array[0];
			string text2 = array[1];
			string name = array[2];
			Assembly assembly = Assembly.Load(text);
			Type type = assembly.GetType(text2, false, false);
			PropertyInfo property = type.GetProperty(name);
			return property.GetValue(null, null).ToString();
		}

		// Token: 0x06000037 RID: 55 RVA: 0x000029CC File Offset: 0x00000BCC
		public static FSharpOption<global::NPCUA.Node> Find(Uri target)
		{
			string absolutePath = target.AbsolutePath;
			return FSharpOption<global::NPCUA.Node>.Some(new global::NPCUA.SystemNode(absolutePath));
		}

		// Token: 0x17000011 RID: 17
		// (get) Token: 0x06000038 RID: 56 RVA: 0x000029EC File Offset: 0x00000BEC
		public override FSharpList<global::NPCUA.AttributeId> Allowed_attributes
		{
			get
			{
				return FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.NodeId, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.NodeClass, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.DisplayName, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.Description, FSharpList<global::NPCUA.AttributeId>.Cons(global::NPCUA.AttributeId.Value, FSharpList<global::NPCUA.AttributeId>.Empty)))));
			}
		}

		// Token: 0x06000039 RID: 57 RVA: 0x00002A14 File Offset: 0x00000C14
		public override FSharpOption<object> Read_attribute(global::NPCUA.AttributeId aid)
		{
			string str = this.path@115.TrimStart('/');
			string text = "System.Private.CoreLib/System." + str;
			if (aid == global::NPCUA.AttributeId.NodeId)
			{
				return FSharpOption<object>.Some("npc://System/" + str);
			}
			if (aid == global::NPCUA.AttributeId.DisplayName)
			{
				return FSharpOption<object>.Some(text);
			}
			if (aid == global::NPCUA.AttributeId.Value)
			{
				return FSharpOption<object>.Some(global::NPCUA.SystemNode.GetSystemProperty(text));
			}
			return null;
		}

		// Token: 0x0600003A RID: 58 RVA: 0x00002A70 File Offset: 0x00000C70
		public override bool Write_attribute(global::NPCUA.AttributeId aid, object v)
		{
			return false;
		}

		// Token: 0x0400000E RID: 14
		internal string path@115;
	}

	// Token: 0x02000008 RID: 8
	[CompilationMapping(3)]
	[Serializable]
	public class NodeManager
	{
		// Token: 0x0600003B RID: 59 RVA: 0x00002A74 File Offset: 0x00000C74
		public NodeManager() : this()
		{
		}

		// Token: 0x0600003C RID: 60 RVA: 0x00002A80 File Offset: 0x00000C80
		public static FSharpOption<global::NPCUA.Node> Find(string target)
		{
			Uri uri = new Uri(target);
			string text = uri.Host.ToLower();
			string host = uri.Host;
			if (!string.Equals(uri.Scheme, "npc"))
			{
				return null;
			}
			if (string.Equals(text, "system"))
			{
				return global::NPCUA.SystemNode.Find(uri);
			}
			if (string.Equals(text, "variable"))
			{
				return global::NPCUA.VariableNode.Find(uri);
			}
			return null;
		}
	}

	// Token: 0x02000009 RID: 9
	[CompilationMapping(3)]
	[Serializable]
	public class BitWriter
	{
		// Token: 0x0600003D RID: 61 RVA: 0x00002AE8 File Offset: 0x00000CE8
		public BitWriter(byte[] data) : this()
		{
			this.pre_data = data;
			this.post_data = Array.Empty<byte>();
		}

		// Token: 0x0600003E RID: 62 RVA: 0x00002B04 File Offset: 0x00000D04
		public byte[] data()
		{
			return ArrayModule.Concat<byte>(FSharpList<byte[]>.Cons(this.pre_data, FSharpList<byte[]>.Cons(this.post_data, FSharpList<byte[]>.Empty)));
		}

		// Token: 0x0600003F RID: 63 RVA: 0x00002B28 File Offset: 0x00000D28
		public int length()
		{
			return this.data().Length;
		}

		// Token: 0x06000040 RID: 64 RVA: 0x00002B34 File Offset: 0x00000D34
		public void append(global::NPCUA.BitWriter bw)
		{
			this.bytes(bw.data());
		}

		// Token: 0x06000041 RID: 65 RVA: 0x00002B44 File Offset: 0x00000D44
		public void append(byte[] data)
		{
			this.pre_data = ArrayModule.Concat<byte>(FSharpList<byte[]>.Cons(this.pre_data, FSharpList<byte[]>.Cons(data, FSharpList<byte[]>.Empty)));
		}

		// Token: 0x06000042 RID: 66 RVA: 0x00002B68 File Offset: 0x00000D68
		public void _set_post_data(byte[] data)
		{
			this.post_data = data;
		}

		// Token: 0x06000043 RID: 67 RVA: 0x00002B74 File Offset: 0x00000D74
		public global::NPCUA.BitWriter prepender()
		{
			return new global::NPCUA.BitWriter(Array.Empty<byte>())
			{
				post_data = this.data()
			};
		}

		// Token: 0x06000044 RID: 68 RVA: 0x00002B9C File Offset: 0x00000D9C
		public global::NPCUA.BitWriter postpender()
		{
			return new global::NPCUA.BitWriter(this.data());
		}

		// Token: 0x06000045 RID: 69 RVA: 0x00002BAC File Offset: 0x00000DAC
		public void write(Stream s)
		{
			s.Write(this.data(), 0, this.data().Length);
		}

		// Token: 0x06000046 RID: 70 RVA: 0x00002BC8 File Offset: 0x00000DC8
		public void bytes(byte[] data)
		{
			this.append(data);
		}

		// Token: 0x06000047 RID: 71 RVA: 0x00002BD4 File Offset: 0x00000DD4
		public void u8(byte i)
		{
			this.append(new byte[]
			{
				i
			});
		}

		// Token: 0x06000048 RID: 72 RVA: 0x00002BEC File Offset: 0x00000DEC
		public void u32(int i)
		{
			this.append(BitConverter.GetBytes(i));
		}

		// Token: 0x06000049 RID: 73 RVA: 0x00002BFC File Offset: 0x00000DFC
		public void u64(long i)
		{
			this.append(BitConverter.GetBytes(i));
		}

		// Token: 0x0600004A RID: 74 RVA: 0x00002C0C File Offset: 0x00000E0C
		public void str(string s)
		{
			byte[] bytes = Encoding.UTF8.GetBytes(s);
			int num = bytes.Length;
			this.append(BitConverter.GetBytes(num));
			this.append(bytes);
		}

		// Token: 0x0600004B RID: 75 RVA: 0x00002C40 File Offset: 0x00000E40
		public void byte_array(byte[] b)
		{
			int num = b.Length;
			this.append(BitConverter.GetBytes(num));
			this.append(b);
		}

		// Token: 0x0400000F RID: 15
		internal byte[] pre_data;

		// Token: 0x04000010 RID: 16
		internal byte[] post_data;
	}

	// Token: 0x0200000A RID: 10
	[CompilationMapping(3)]
	[Serializable]
	public class BitReader
	{
		// Token: 0x0600004C RID: 76 RVA: 0x00002C68 File Offset: 0x00000E68
		public BitReader(byte[] data) : this()
		{
			this.data@262 = data;
			this.offset = new FSharpRef<int>(0);
		}

		// Token: 0x0600004D RID: 77 RVA: 0x00002C88 File Offset: 0x00000E88
		public byte[] bytes(int length)
		{
			if (length <= 0)
			{
				return Array.Empty<byte>();
			}
			byte[] array = this.data@262;
			int contents = this.offset.contents;
			int num = this.offset.contents + length - 1;
			int num2 = array.Length;
			int num3 = (contents < 0) ? 0 : contents;
			int num4 = (num >= 0 + num2) ? (0 + num2 - 1) : num;
			int num5 = num4 - num3 + 1;
			int num6 = (num5 >= 0) ? num5 : 0;
			byte[] array2 = new byte[num6];
			int num7 = 0;
			int num8 = num6 - 1;
			if (num8 >= num7)
			{
				do
				{
					array2[num7] = array[num3 + num7];
					num7++;
				}
				while (num7 != num8 + 1);
			}
			byte[] result = array2;
			this.offset.contents = this.offset.contents + length;
			return result;
		}

		// Token: 0x0600004E RID: 78 RVA: 0x00002D58 File Offset: 0x00000F58
		public uint u32()
		{
			return BitConverter.ToUInt32(this.bytes(4), 0);
		}

		// Token: 0x0600004F RID: 79 RVA: 0x00002D68 File Offset: 0x00000F68
		public ulong u64()
		{
			return BitConverter.ToUInt64(this.bytes(8), 0);
		}

		// Token: 0x06000050 RID: 80 RVA: 0x00002D78 File Offset: 0x00000F78
		public ushort u16()
		{
			return BitConverter.ToUInt16(this.bytes(2), 0);
		}

		// Token: 0x06000051 RID: 81 RVA: 0x00002D88 File Offset: 0x00000F88
		public byte[] byte_str()
		{
			uint length = BitConverter.ToUInt32(this.bytes(4), 0);
			return this.bytes((int)length);
		}

		// Token: 0x06000052 RID: 82 RVA: 0x00002DAC File Offset: 0x00000FAC
		public string str()
		{
			uint length = BitConverter.ToUInt32(this.bytes(4), 0);
			byte[] array = this.bytes((int)length);
			return Encoding.UTF8.GetString(array);
		}

		// Token: 0x06000053 RID: 83 RVA: 0x00002DDC File Offset: 0x00000FDC
		public string qualified_name()
		{
			ushort num = BitConverter.ToUInt16(this.bytes(2), 0);
			uint length = BitConverter.ToUInt32(this.bytes(4), 0);
			byte[] array = this.bytes((int)length);
			return Encoding.UTF8.GetString(array);
		}

		// Token: 0x06000054 RID: 84 RVA: 0x00002E1C File Offset: 0x0000101C
		public byte[] rest()
		{
			return this.bytes(this.data@262.Length - this.offset.contents);
		}

		// Token: 0x06000055 RID: 85 RVA: 0x00002E38 File Offset: 0x00001038
		public string node_id()
		{
			uint num = BitConverter.ToUInt32(this.bytes(4), 0);
			if (num == 0U)
			{
				return BitConverter.ToUInt32(this.bytes(4), 0).ToString();
			}
			if (num == 1U)
			{
				uint length = BitConverter.ToUInt32(this.bytes(4), 0);
				byte[] array = this.bytes((int)length);
				return Encoding.UTF8.GetString(array);
			}
			if (num == 2U)
			{
				byte[] array = this.bytes(16);
				return new Guid(array).ToString();
			}
			if (num == 3U)
			{
				return null;
			}
			return null;
		}

		// Token: 0x04000011 RID: 17
		internal byte[] data@262;

		// Token: 0x04000012 RID: 18
		internal FSharpRef<int> offset;
	}

	// Token: 0x0200000B RID: 11
	[CompilationMapping(2)]
	[Serializable]
	public sealed class RequestHeader : IEquatable<global::NPCUA.RequestHeader>, IStructuralEquatable, IComparable<global::NPCUA.RequestHeader>, IComparable, IStructuralComparable
	{
		// Token: 0x17000012 RID: 18
		// (get) Token: 0x06000056 RID: 86 RVA: 0x00002EC8 File Offset: 0x000010C8
		[CompilationMapping(4, 0)]
		public FSharpOption<string> authToken
		{
			get
			{
				return this.authToken@;
			}
		}

		// Token: 0x17000013 RID: 19
		// (get) Token: 0x06000057 RID: 87 RVA: 0x00002ED0 File Offset: 0x000010D0
		[CompilationMapping(4, 1)]
		public long timestamp
		{
			get
			{
				return this.timestamp@;
			}
		}

		// Token: 0x17000014 RID: 20
		// (get) Token: 0x06000058 RID: 88 RVA: 0x00002ED8 File Offset: 0x000010D8
		[CompilationMapping(4, 2)]
		public int requestHandle
		{
			get
			{
				return this.requestHandle@;
			}
		}

		// Token: 0x17000015 RID: 21
		// (get) Token: 0x06000059 RID: 89 RVA: 0x00002EE0 File Offset: 0x000010E0
		[CompilationMapping(4, 3)]
		public FSharpOption<int> returnDiagnostics
		{
			get
			{
				return this.returnDiagnostics@;
			}
		}

		// Token: 0x17000016 RID: 22
		// (get) Token: 0x0600005A RID: 90 RVA: 0x00002EE8 File Offset: 0x000010E8
		[CompilationMapping(4, 4)]
		public FSharpOption<string> auditEntryId
		{
			get
			{
				return this.auditEntryId@;
			}
		}

		// Token: 0x17000017 RID: 23
		// (get) Token: 0x0600005B RID: 91 RVA: 0x00002EF0 File Offset: 0x000010F0
		[CompilationMapping(4, 5)]
		public FSharpOption<int> timeoutHint
		{
			get
			{
				return this.timeoutHint@;
			}
		}

		// Token: 0x0600005C RID: 92 RVA: 0x00002EF8 File Offset: 0x000010F8
		public RequestHeader(FSharpOption<string> authToken, long timestamp, int requestHandle, FSharpOption<int> returnDiagnostics, FSharpOption<string> auditEntryId, FSharpOption<int> timeoutHint)
		{
			this.authToken@ = authToken;
			this.timestamp@ = timestamp;
			this.requestHandle@ = requestHandle;
			this.returnDiagnostics@ = returnDiagnostics;
			this.auditEntryId@ = auditEntryId;
			this.timeoutHint@ = timeoutHint;
		}

		// Token: 0x0600005D RID: 93 RVA: 0x00002F30 File Offset: 0x00001130
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.RequestHeader, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.RequestHeader, string>, Unit, string, string, global::NPCUA.RequestHeader>("%+A")).Invoke(this);
		}

		// Token: 0x0600005E RID: 94 RVA: 0x00002F48 File Offset: 0x00001148
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.RequestHeader obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				int num = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(LanguagePrimitives.GenericComparer, this.authToken@, obj.authToken@);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				return global::NPCUA.CompareTo$cont@346(this, obj, null);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x0600005F RID: 95 RVA: 0x00002F94 File Offset: 0x00001194
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.RequestHeader)obj);
		}

		// Token: 0x06000060 RID: 96 RVA: 0x00002FA4 File Offset: 0x000011A4
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.RequestHeader requestHeader = (global::NPCUA.RequestHeader)obj;
			if (this != null)
			{
				if ((global::NPCUA.RequestHeader)obj == null)
				{
					return 1;
				}
				int num = LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(comp, this.authToken@, requestHeader.authToken@);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				return global::NPCUA.CompareTo$cont@346-1(comp, this, requestHeader, null);
			}
			else
			{
				if ((global::NPCUA.RequestHeader)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000061 RID: 97 RVA: 0x00002FFC File Offset: 0x000011FC
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<int>>(comp, this.timeoutHint@) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<string>>(comp, this.auditEntryId@) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<int>>(comp, this.returnDiagnostics@) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (this.requestHandle@ + ((num << 6) + (num >> 2)));
				int num2 = -1640531527;
				long num3 = this.timestamp@;
				num = num2 + (((int)num3 ^ (int)(num3 >> 32)) + ((num << 6) + (num >> 2)));
				return -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<string>>(comp, this.authToken@) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x06000062 RID: 98 RVA: 0x000030B4 File Offset: 0x000012B4
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x06000063 RID: 99 RVA: 0x000030C4 File Offset: 0x000012C4
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.RequestHeader requestHeader = obj as global::NPCUA.RequestHeader;
				return requestHeader != null && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<string>>(comp, this.authToken@, requestHeader.authToken@) && this.timestamp@ == requestHeader.timestamp@ && this.requestHandle@ == requestHeader.requestHandle@ && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<int>>(comp, this.returnDiagnostics@, requestHeader.returnDiagnostics@) && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<string>>(comp, this.auditEntryId@, requestHeader.auditEntryId@) && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<int>>(comp, this.timeoutHint@, requestHeader.timeoutHint@);
			}
			return obj == null;
		}

		// Token: 0x06000064 RID: 100 RVA: 0x00003164 File Offset: 0x00001364
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.RequestHeader obj)
		{
			if (this != null)
			{
				return obj != null && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<string>>(this.authToken@, obj.authToken@) && this.timestamp@ == obj.timestamp@ && this.requestHandle@ == obj.requestHandle@ && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<int>>(this.returnDiagnostics@, obj.returnDiagnostics@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<string>>(this.auditEntryId@, obj.auditEntryId@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<int>>(this.timeoutHint@, obj.timeoutHint@);
			}
			return obj == null;
		}

		// Token: 0x06000065 RID: 101 RVA: 0x000031FC File Offset: 0x000013FC
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.RequestHeader requestHeader = obj as global::NPCUA.RequestHeader;
			return requestHeader != null && this.Equals(requestHeader);
		}

		// Token: 0x04000013 RID: 19
		[DebuggerBrowsable(0)]
		internal FSharpOption<string> authToken@;

		// Token: 0x04000014 RID: 20
		[DebuggerBrowsable(0)]
		internal long timestamp@;

		// Token: 0x04000015 RID: 21
		[DebuggerBrowsable(0)]
		internal int requestHandle@;

		// Token: 0x04000016 RID: 22
		[DebuggerBrowsable(0)]
		internal FSharpOption<int> returnDiagnostics@;

		// Token: 0x04000017 RID: 23
		[DebuggerBrowsable(0)]
		internal FSharpOption<string> auditEntryId@;

		// Token: 0x04000018 RID: 24
		[DebuggerBrowsable(0)]
		internal FSharpOption<int> timeoutHint@;
	}

	// Token: 0x0200000C RID: 12
	[CompilationMapping(2)]
	[Serializable]
	public sealed class ResponseHeader : IEquatable<global::NPCUA.ResponseHeader>, IStructuralEquatable
	{
		// Token: 0x17000018 RID: 24
		// (get) Token: 0x06000066 RID: 102 RVA: 0x00003220 File Offset: 0x00001420
		[CompilationMapping(4, 0)]
		public long timestamp
		{
			get
			{
				return this.timestamp@;
			}
		}

		// Token: 0x17000019 RID: 25
		// (get) Token: 0x06000067 RID: 103 RVA: 0x00003228 File Offset: 0x00001428
		[CompilationMapping(4, 1)]
		public int requestHandle
		{
			get
			{
				return this.requestHandle@;
			}
		}

		// Token: 0x1700001A RID: 26
		// (get) Token: 0x06000068 RID: 104 RVA: 0x00003230 File Offset: 0x00001430
		[CompilationMapping(4, 2)]
		public uint serviceResult
		{
			get
			{
				return this.serviceResult@;
			}
		}

		// Token: 0x1700001B RID: 27
		// (get) Token: 0x06000069 RID: 105 RVA: 0x00003238 File Offset: 0x00001438
		[CompilationMapping(4, 3)]
		public FSharpOption<object> serviceDiagnostics
		{
			get
			{
				return this.serviceDiagnostics@;
			}
		}

		// Token: 0x1700001C RID: 28
		// (get) Token: 0x0600006A RID: 106 RVA: 0x00003240 File Offset: 0x00001440
		[CompilationMapping(4, 4)]
		public string[] stringTable
		{
			get
			{
				return this.stringTable@;
			}
		}

		// Token: 0x0600006B RID: 107 RVA: 0x00003248 File Offset: 0x00001448
		public ResponseHeader(long timestamp, int requestHandle, uint serviceResult, FSharpOption<object> serviceDiagnostics, string[] stringTable)
		{
			this.timestamp@ = timestamp;
			this.requestHandle@ = requestHandle;
			this.serviceResult@ = serviceResult;
			this.serviceDiagnostics@ = serviceDiagnostics;
			this.stringTable@ = stringTable;
		}

		// Token: 0x0600006C RID: 108 RVA: 0x00003278 File Offset: 0x00001478
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.ResponseHeader, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.ResponseHeader, string>, Unit, string, string, global::NPCUA.ResponseHeader>("%+A")).Invoke(this);
		}

		// Token: 0x0600006D RID: 109 RVA: 0x00003290 File Offset: 0x00001490
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<string[]>(comp, this.stringTable@) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<object>>(comp, this.serviceDiagnostics@) + ((num << 6) + (num >> 2)));
				num = (int)(2654435769U + (this.serviceResult@ + (uint)((num << 6) + (num >> 2))));
				num = -1640531527 + (this.requestHandle@ + ((num << 6) + (num >> 2)));
				int num2 = -1640531527;
				long num3 = this.timestamp@;
				return num2 + (((int)num3 ^ (int)(num3 >> 32)) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x0600006E RID: 110 RVA: 0x00003328 File Offset: 0x00001528
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x0600006F RID: 111 RVA: 0x00003338 File Offset: 0x00001538
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.ResponseHeader responseHeader = obj as global::NPCUA.ResponseHeader;
				return responseHeader != null && this.timestamp@ == responseHeader.timestamp@ && this.requestHandle@ == responseHeader.requestHandle@ && this.serviceResult@ == responseHeader.serviceResult@ && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<object>>(comp, this.serviceDiagnostics@, responseHeader.serviceDiagnostics@) && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<string[]>(comp, this.stringTable@, responseHeader.stringTable@);
			}
			return obj == null;
		}

		// Token: 0x06000070 RID: 112 RVA: 0x000033B8 File Offset: 0x000015B8
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.ResponseHeader obj)
		{
			if (this != null)
			{
				return obj != null && this.timestamp@ == obj.timestamp@ && this.requestHandle@ == obj.requestHandle@ && this.serviceResult@ == obj.serviceResult@ && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<object>>(this.serviceDiagnostics@, obj.serviceDiagnostics@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<string[]>(this.stringTable@, obj.stringTable@);
			}
			return obj == null;
		}

		// Token: 0x06000071 RID: 113 RVA: 0x00003430 File Offset: 0x00001630
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.ResponseHeader responseHeader = obj as global::NPCUA.ResponseHeader;
			return responseHeader != null && this.Equals(responseHeader);
		}

		// Token: 0x04000019 RID: 25
		[DebuggerBrowsable(0)]
		internal long timestamp@;

		// Token: 0x0400001A RID: 26
		[DebuggerBrowsable(0)]
		internal int requestHandle@;

		// Token: 0x0400001B RID: 27
		[DebuggerBrowsable(0)]
		internal uint serviceResult@;

		// Token: 0x0400001C RID: 28
		[DebuggerBrowsable(0)]
		internal FSharpOption<object> serviceDiagnostics@;

		// Token: 0x0400001D RID: 29
		[DebuggerBrowsable(0)]
		internal string[] stringTable@;
	}

	// Token: 0x0200000D RID: 13
	[CompilationMapping(2)]
	[Serializable]
	public sealed class NodeId : IEquatable<global::NPCUA.NodeId>, IStructuralEquatable, IComparable<global::NPCUA.NodeId>, IComparable, IStructuralComparable
	{
		// Token: 0x1700001D RID: 29
		// (get) Token: 0x06000072 RID: 114 RVA: 0x00003454 File Offset: 0x00001654
		[CompilationMapping(4, 0)]
		public int IdType
		{
			get
			{
				return this.IdType@;
			}
		}

		// Token: 0x1700001E RID: 30
		// (get) Token: 0x06000073 RID: 115 RVA: 0x0000345C File Offset: 0x0000165C
		[CompilationMapping(4, 1)]
		public string Id
		{
			get
			{
				return this.Id@;
			}
		}

		// Token: 0x06000074 RID: 116 RVA: 0x00003464 File Offset: 0x00001664
		public NodeId(int idType, string id)
		{
			this.IdType@ = idType;
			this.Id@ = id;
		}

		// Token: 0x06000075 RID: 117 RVA: 0x0000347C File Offset: 0x0000167C
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.NodeId, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.NodeId, string>, Unit, string, string, global::NPCUA.NodeId>("%+A")).Invoke(this);
		}

		// Token: 0x06000076 RID: 118 RVA: 0x00003494 File Offset: 0x00001694
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.NodeId obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				IComparer genericComparer = LanguagePrimitives.GenericComparer;
				int idType@ = this.IdType@;
				int idType@2 = obj.IdType@;
				int num = ((idType@ > idType@2) - (idType@ < idType@2)) ? 1 : 0;
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				return string.CompareOrdinal(this.Id@, obj.Id@);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000077 RID: 119 RVA: 0x000034F4 File Offset: 0x000016F4
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.NodeId)obj);
		}

		// Token: 0x06000078 RID: 120 RVA: 0x00003504 File Offset: 0x00001704
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.NodeId nodeId = (global::NPCUA.NodeId)obj;
			if (this != null)
			{
				if ((global::NPCUA.NodeId)obj == null)
				{
					return 1;
				}
				int idType@ = this.IdType@;
				int idType@2 = nodeId.IdType@;
				int num = ((idType@ > idType@2) - (idType@ < idType@2)) ? 1 : 0;
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				return string.CompareOrdinal(this.Id@, nodeId.Id@);
			}
			else
			{
				if ((global::NPCUA.NodeId)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000079 RID: 121 RVA: 0x00003568 File Offset: 0x00001768
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				int num2 = -1640531527;
				string id@ = this.Id@;
				num = num2 + (((id@ != null) ? id@.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
				return -1640531527 + (this.IdType@ + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x0600007A RID: 122 RVA: 0x000035B8 File Offset: 0x000017B8
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x0600007B RID: 123 RVA: 0x000035C8 File Offset: 0x000017C8
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.NodeId nodeId = obj as global::NPCUA.NodeId;
				return nodeId != null && this.IdType@ == nodeId.IdType@ && string.Equals(this.Id@, nodeId.Id@);
			}
			return obj == null;
		}

		// Token: 0x0600007C RID: 124 RVA: 0x00003610 File Offset: 0x00001810
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.NodeId obj)
		{
			if (this != null)
			{
				return obj != null && this.IdType@ == obj.IdType@ && string.Equals(this.Id@, obj.Id@);
			}
			return obj == null;
		}

		// Token: 0x0600007D RID: 125 RVA: 0x00003644 File Offset: 0x00001844
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.NodeId nodeId = obj as global::NPCUA.NodeId;
			return nodeId != null && this.Equals(nodeId);
		}

		// Token: 0x0400001E RID: 30
		[DebuggerBrowsable(0)]
		internal int IdType@;

		// Token: 0x0400001F RID: 31
		[DebuggerBrowsable(0)]
		internal string Id@;
	}

	// Token: 0x0200000E RID: 14
	[CompilationMapping(2)]
	[Serializable]
	public sealed class ReadValue : IEquatable<global::NPCUA.ReadValue>, IStructuralEquatable, IComparable<global::NPCUA.ReadValue>, IComparable, IStructuralComparable
	{
		// Token: 0x1700001F RID: 31
		// (get) Token: 0x0600007E RID: 126 RVA: 0x00003664 File Offset: 0x00001864
		[CompilationMapping(4, 0)]
		public global::NPCUA.NodeId nodeId
		{
			get
			{
				return this.nodeId@;
			}
		}

		// Token: 0x17000020 RID: 32
		// (get) Token: 0x0600007F RID: 127 RVA: 0x0000366C File Offset: 0x0000186C
		[CompilationMapping(4, 1)]
		public int attributeId
		{
			get
			{
				return this.attributeId@;
			}
		}

		// Token: 0x17000021 RID: 33
		// (get) Token: 0x06000080 RID: 128 RVA: 0x00003674 File Offset: 0x00001874
		[CompilationMapping(4, 2)]
		public string indexRange
		{
			get
			{
				return this.indexRange@;
			}
		}

		// Token: 0x17000022 RID: 34
		// (get) Token: 0x06000081 RID: 129 RVA: 0x0000367C File Offset: 0x0000187C
		[CompilationMapping(4, 3)]
		public string dataEncoding
		{
			get
			{
				return this.dataEncoding@;
			}
		}

		// Token: 0x06000082 RID: 130 RVA: 0x00003684 File Offset: 0x00001884
		public ReadValue(global::NPCUA.NodeId nodeId, int attributeId, string indexRange, string dataEncoding)
		{
			this.nodeId@ = nodeId;
			this.attributeId@ = attributeId;
			this.indexRange@ = indexRange;
			this.dataEncoding@ = dataEncoding;
		}

		// Token: 0x06000083 RID: 131 RVA: 0x000036AC File Offset: 0x000018AC
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.ReadValue, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.ReadValue, string>, Unit, string, string, global::NPCUA.ReadValue>("%+A")).Invoke(this);
		}

		// Token: 0x06000084 RID: 132 RVA: 0x000036C4 File Offset: 0x000018C4
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.ReadValue obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				IComparer genericComparer = LanguagePrimitives.GenericComparer;
				global::NPCUA.NodeId nodeId = this.nodeId@;
				global::NPCUA.NodeId obj2 = obj.nodeId@;
				int num = nodeId.CompareTo(obj2, genericComparer);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				int num2 = this.attributeId@;
				int num3 = obj.attributeId@;
				int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
				if (num4 < 0)
				{
					return num4;
				}
				if (num4 > 0)
				{
					return num4;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				num2 = string.CompareOrdinal(this.indexRange@, obj.indexRange@);
				if (num2 < 0)
				{
					return num2;
				}
				if (num2 > 0)
				{
					return num2;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				return string.CompareOrdinal(this.dataEncoding@, obj.dataEncoding@);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000085 RID: 133 RVA: 0x00003784 File Offset: 0x00001984
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.ReadValue)obj);
		}

		// Token: 0x06000086 RID: 134 RVA: 0x00003794 File Offset: 0x00001994
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.ReadValue readValue = (global::NPCUA.ReadValue)obj;
			if (this != null)
			{
				if ((global::NPCUA.ReadValue)obj == null)
				{
					return 1;
				}
				global::NPCUA.NodeId nodeId = this.nodeId@;
				global::NPCUA.NodeId obj2 = readValue.nodeId@;
				int num = nodeId.CompareTo(obj2, comp);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				int num2 = this.attributeId@;
				int num3 = readValue.attributeId@;
				int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
				if (num4 < 0)
				{
					return num4;
				}
				if (num4 > 0)
				{
					return num4;
				}
				num2 = string.CompareOrdinal(this.indexRange@, readValue.indexRange@);
				if (num2 < 0)
				{
					return num2;
				}
				if (num2 > 0)
				{
					return num2;
				}
				return string.CompareOrdinal(this.dataEncoding@, readValue.dataEncoding@);
			}
			else
			{
				if ((global::NPCUA.ReadValue)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000087 RID: 135 RVA: 0x00003850 File Offset: 0x00001A50
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				int num2 = -1640531527;
				string text = this.dataEncoding@;
				num = num2 + (((text != null) ? text.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
				int num3 = -1640531527;
				text = this.indexRange@;
				num = num3 + (((text != null) ? text.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (this.attributeId@ + ((num << 6) + (num >> 2)));
				return -1640531527 + (this.nodeId@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x06000088 RID: 136 RVA: 0x000038E0 File Offset: 0x00001AE0
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x06000089 RID: 137 RVA: 0x000038F0 File Offset: 0x00001AF0
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this == null)
			{
				return obj == null;
			}
			global::NPCUA.ReadValue readValue = obj as global::NPCUA.ReadValue;
			if (readValue != null)
			{
				global::NPCUA.NodeId nodeId = this.nodeId@;
				global::NPCUA.NodeId obj2 = readValue.nodeId@;
				return nodeId.Equals(obj2, comp) && this.attributeId@ == readValue.attributeId@ && string.Equals(this.indexRange@, readValue.indexRange@) && string.Equals(this.dataEncoding@, readValue.dataEncoding@);
			}
			return false;
		}

		// Token: 0x0600008A RID: 138 RVA: 0x00003964 File Offset: 0x00001B64
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.ReadValue obj)
		{
			if (this != null)
			{
				return obj != null && this.nodeId@.Equals(obj.nodeId@) && this.attributeId@ == obj.attributeId@ && string.Equals(this.indexRange@, obj.indexRange@) && string.Equals(this.dataEncoding@, obj.dataEncoding@);
			}
			return obj == null;
		}

		// Token: 0x0600008B RID: 139 RVA: 0x000039CC File Offset: 0x00001BCC
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.ReadValue readValue = obj as global::NPCUA.ReadValue;
			return readValue != null && this.Equals(readValue);
		}

		// Token: 0x04000020 RID: 32
		[DebuggerBrowsable(0)]
		internal global::NPCUA.NodeId nodeId@;

		// Token: 0x04000021 RID: 33
		[DebuggerBrowsable(0)]
		internal int attributeId@;

		// Token: 0x04000022 RID: 34
		[DebuggerBrowsable(0)]
		internal string indexRange@;

		// Token: 0x04000023 RID: 35
		[DebuggerBrowsable(0)]
		internal string dataEncoding@;
	}

	// Token: 0x0200000F RID: 15
	[CompilationMapping(2)]
	[Serializable]
	public sealed class ReadService : IEquatable<global::NPCUA.ReadService>, IStructuralEquatable, IComparable<global::NPCUA.ReadService>, IComparable, IStructuralComparable
	{
		// Token: 0x17000023 RID: 35
		// (get) Token: 0x0600008C RID: 140 RVA: 0x000039EC File Offset: 0x00001BEC
		[CompilationMapping(4, 0)]
		public global::NPCUA.RequestHeader requestHeader
		{
			get
			{
				return this.requestHeader@;
			}
		}

		// Token: 0x17000024 RID: 36
		// (get) Token: 0x0600008D RID: 141 RVA: 0x000039F4 File Offset: 0x00001BF4
		[CompilationMapping(4, 1)]
		public int maxAge
		{
			get
			{
				return this.maxAge@;
			}
		}

		// Token: 0x17000025 RID: 37
		// (get) Token: 0x0600008E RID: 142 RVA: 0x000039FC File Offset: 0x00001BFC
		[CompilationMapping(4, 2)]
		public int timestampsToReturn
		{
			get
			{
				return this.timestampsToReturn@;
			}
		}

		// Token: 0x17000026 RID: 38
		// (get) Token: 0x0600008F RID: 143 RVA: 0x00003A04 File Offset: 0x00001C04
		[CompilationMapping(4, 3)]
		public global::NPCUA.ReadValue[] nodesToRead
		{
			get
			{
				return this.nodesToRead@;
			}
		}

		// Token: 0x06000090 RID: 144 RVA: 0x00003A0C File Offset: 0x00001C0C
		public ReadService(global::NPCUA.RequestHeader requestHeader, int maxAge, int timestampsToReturn, global::NPCUA.ReadValue[] nodesToRead)
		{
			this.requestHeader@ = requestHeader;
			this.maxAge@ = maxAge;
			this.timestampsToReturn@ = timestampsToReturn;
			this.nodesToRead@ = nodesToRead;
		}

		// Token: 0x06000091 RID: 145 RVA: 0x00003A34 File Offset: 0x00001C34
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.ReadService, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.ReadService, string>, Unit, string, string, global::NPCUA.ReadService>("%+A")).Invoke(this);
		}

		// Token: 0x06000092 RID: 146 RVA: 0x00003A4C File Offset: 0x00001C4C
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.ReadService obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				IComparer genericComparer = LanguagePrimitives.GenericComparer;
				global::NPCUA.RequestHeader requestHeader = this.requestHeader@;
				global::NPCUA.RequestHeader obj2 = obj.requestHeader@;
				int num = requestHeader.CompareTo(obj2, genericComparer);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				int num2 = this.maxAge@;
				int num3 = obj.maxAge@;
				int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
				if (num4 < 0)
				{
					return num4;
				}
				if (num4 > 0)
				{
					return num4;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				num3 = this.timestampsToReturn@;
				int num5 = obj.timestampsToReturn@;
				num2 = (((num3 > num5) - (num3 < num5)) ? 1 : 0);
				if (num2 < 0)
				{
					return num2;
				}
				if (num2 > 0)
				{
					return num2;
				}
				return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<global::NPCUA.ReadValue[]>(LanguagePrimitives.GenericComparer, this.nodesToRead@, obj.nodesToRead@);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000093 RID: 147 RVA: 0x00003B1C File Offset: 0x00001D1C
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.ReadService)obj);
		}

		// Token: 0x06000094 RID: 148 RVA: 0x00003B2C File Offset: 0x00001D2C
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.ReadService readService = (global::NPCUA.ReadService)obj;
			if (this != null)
			{
				if ((global::NPCUA.ReadService)obj == null)
				{
					return 1;
				}
				global::NPCUA.RequestHeader requestHeader = this.requestHeader@;
				global::NPCUA.RequestHeader obj2 = readService.requestHeader@;
				int num = requestHeader.CompareTo(obj2, comp);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				int num2 = this.maxAge@;
				int num3 = readService.maxAge@;
				int num4 = ((num2 > num3) - (num2 < num3)) ? 1 : 0;
				if (num4 < 0)
				{
					return num4;
				}
				if (num4 > 0)
				{
					return num4;
				}
				num3 = this.timestampsToReturn@;
				int num5 = readService.timestampsToReturn@;
				num2 = (((num3 > num5) - (num3 < num5)) ? 1 : 0);
				if (num2 < 0)
				{
					return num2;
				}
				if (num2 > 0)
				{
					return num2;
				}
				return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<global::NPCUA.ReadValue[]>(comp, this.nodesToRead@, readService.nodesToRead@);
			}
			else
			{
				if ((global::NPCUA.ReadService)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x06000095 RID: 149 RVA: 0x00003BF4 File Offset: 0x00001DF4
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<global::NPCUA.ReadValue[]>(comp, this.nodesToRead@) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (this.timestampsToReturn@ + ((num << 6) + (num >> 2)));
				num = -1640531527 + (this.maxAge@ + ((num << 6) + (num >> 2)));
				return -1640531527 + (this.requestHeader@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x06000096 RID: 150 RVA: 0x00003C6C File Offset: 0x00001E6C
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x06000097 RID: 151 RVA: 0x00003C7C File Offset: 0x00001E7C
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this == null)
			{
				return obj == null;
			}
			global::NPCUA.ReadService readService = obj as global::NPCUA.ReadService;
			if (readService != null)
			{
				global::NPCUA.RequestHeader requestHeader = this.requestHeader@;
				global::NPCUA.RequestHeader obj2 = readService.requestHeader@;
				return requestHeader.Equals(obj2, comp) && this.maxAge@ == readService.maxAge@ && this.timestampsToReturn@ == readService.timestampsToReturn@ && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<global::NPCUA.ReadValue[]>(comp, this.nodesToRead@, readService.nodesToRead@);
			}
			return false;
		}

		// Token: 0x06000098 RID: 152 RVA: 0x00003CF0 File Offset: 0x00001EF0
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.ReadService obj)
		{
			if (this != null)
			{
				return obj != null && this.requestHeader@.Equals(obj.requestHeader@) && this.maxAge@ == obj.maxAge@ && this.timestampsToReturn@ == obj.timestampsToReturn@ && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<global::NPCUA.ReadValue[]>(this.nodesToRead@, obj.nodesToRead@);
			}
			return obj == null;
		}

		// Token: 0x06000099 RID: 153 RVA: 0x00003D58 File Offset: 0x00001F58
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.ReadService readService = obj as global::NPCUA.ReadService;
			return readService != null && this.Equals(readService);
		}

		// Token: 0x04000024 RID: 36
		[DebuggerBrowsable(0)]
		internal global::NPCUA.RequestHeader requestHeader@;

		// Token: 0x04000025 RID: 37
		[DebuggerBrowsable(0)]
		internal int maxAge@;

		// Token: 0x04000026 RID: 38
		[DebuggerBrowsable(0)]
		internal int timestampsToReturn@;

		// Token: 0x04000027 RID: 39
		[DebuggerBrowsable(0)]
		internal global::NPCUA.ReadValue[] nodesToRead@;
	}

	// Token: 0x02000010 RID: 16
	[CompilationMapping(2)]
	[Serializable]
	public sealed class SignedData : IEquatable<global::NPCUA.SignedData>, IStructuralEquatable, IComparable<global::NPCUA.SignedData>, IComparable, IStructuralComparable
	{
		// Token: 0x17000027 RID: 39
		// (get) Token: 0x0600009A RID: 154 RVA: 0x00003D7C File Offset: 0x00001F7C
		[CompilationMapping(4, 0)]
		public string data
		{
			get
			{
				return this.data@;
			}
		}

		// Token: 0x17000028 RID: 40
		// (get) Token: 0x0600009B RID: 155 RVA: 0x00003D84 File Offset: 0x00001F84
		[CompilationMapping(4, 1)]
		public string signature
		{
			get
			{
				return this.signature@;
			}
		}

		// Token: 0x0600009C RID: 156 RVA: 0x00003D8C File Offset: 0x00001F8C
		public SignedData(string data, string signature)
		{
			this.data@ = data;
			this.signature@ = signature;
		}

		// Token: 0x0600009D RID: 157 RVA: 0x00003DA4 File Offset: 0x00001FA4
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.SignedData, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.SignedData, string>, Unit, string, string, global::NPCUA.SignedData>("%+A")).Invoke(this);
		}

		// Token: 0x0600009E RID: 158 RVA: 0x00003DBC File Offset: 0x00001FBC
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.SignedData obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				IComparer genericComparer = LanguagePrimitives.GenericComparer;
				int num = string.CompareOrdinal(this.data@, obj.data@);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				genericComparer = LanguagePrimitives.GenericComparer;
				return string.CompareOrdinal(this.signature@, obj.signature@);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x0600009F RID: 159 RVA: 0x00003E14 File Offset: 0x00002014
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.SignedData)obj);
		}

		// Token: 0x060000A0 RID: 160 RVA: 0x00003E24 File Offset: 0x00002024
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.SignedData signedData = (global::NPCUA.SignedData)obj;
			if (this != null)
			{
				if ((global::NPCUA.SignedData)obj == null)
				{
					return 1;
				}
				int num = string.CompareOrdinal(this.data@, signedData.data@);
				if (num < 0)
				{
					return num;
				}
				if (num > 0)
				{
					return num;
				}
				return string.CompareOrdinal(this.signature@, signedData.signature@);
			}
			else
			{
				if ((global::NPCUA.SignedData)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x060000A1 RID: 161 RVA: 0x00003E80 File Offset: 0x00002080
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				int num2 = -1640531527;
				string text = this.signature@;
				num = num2 + (((text != null) ? text.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
				int num3 = -1640531527;
				text = this.data@;
				return num3 + (((text != null) ? text.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x060000A2 RID: 162 RVA: 0x00003EE0 File Offset: 0x000020E0
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x060000A3 RID: 163 RVA: 0x00003EF0 File Offset: 0x000020F0
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.SignedData signedData = obj as global::NPCUA.SignedData;
				return signedData != null && string.Equals(this.data@, signedData.data@) && string.Equals(this.signature@, signedData.signature@);
			}
			return obj == null;
		}

		// Token: 0x060000A4 RID: 164 RVA: 0x00003F3C File Offset: 0x0000213C
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.SignedData obj)
		{
			if (this != null)
			{
				return obj != null && string.Equals(this.data@, obj.data@) && string.Equals(this.signature@, obj.signature@);
			}
			return obj == null;
		}

		// Token: 0x060000A5 RID: 165 RVA: 0x00003F74 File Offset: 0x00002174
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.SignedData signedData = obj as global::NPCUA.SignedData;
			return signedData != null && this.Equals(signedData);
		}

		// Token: 0x04000028 RID: 40
		[DebuggerBrowsable(0)]
		internal string data@;

		// Token: 0x04000029 RID: 41
		[DebuggerBrowsable(0)]
		internal string signature@;
	}

	// Token: 0x02000011 RID: 17
	[CompilationMapping(2)]
	[Serializable]
	public sealed class ListResultsResponse : IEquatable<global::NPCUA.ListResultsResponse>, IStructuralEquatable
	{
		// Token: 0x17000029 RID: 41
		// (get) Token: 0x060000A6 RID: 166 RVA: 0x00003F94 File Offset: 0x00002194
		[CompilationMapping(4, 0)]
		public global::NPCUA.ResponseHeader responseHeader
		{
			get
			{
				return this.responseHeader@;
			}
		}

		// Token: 0x1700002A RID: 42
		// (get) Token: 0x060000A7 RID: 167 RVA: 0x00003F9C File Offset: 0x0000219C
		[CompilationMapping(4, 1)]
		public FSharpList<object> results
		{
			get
			{
				return this.results@;
			}
		}

		// Token: 0x1700002B RID: 43
		// (get) Token: 0x060000A8 RID: 168 RVA: 0x00003FA4 File Offset: 0x000021A4
		[CompilationMapping(4, 2)]
		public FSharpList<object> diagnosticInfos
		{
			get
			{
				return this.diagnosticInfos@;
			}
		}

		// Token: 0x060000A9 RID: 169 RVA: 0x00003FAC File Offset: 0x000021AC
		public ListResultsResponse(global::NPCUA.ResponseHeader responseHeader, FSharpList<object> results, FSharpList<object> diagnosticInfos)
		{
			this.responseHeader@ = responseHeader;
			this.results@ = results;
			this.diagnosticInfos@ = diagnosticInfos;
		}

		// Token: 0x060000AA RID: 170 RVA: 0x00003FCC File Offset: 0x000021CC
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.ListResultsResponse, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.ListResultsResponse, string>, Unit, string, string, global::NPCUA.ListResultsResponse>("%+A")).Invoke(this);
		}

		// Token: 0x060000AB RID: 171 RVA: 0x00003FE4 File Offset: 0x000021E4
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (this.diagnosticInfos@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
				num = -1640531527 + (this.results@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
				return -1640531527 + (this.responseHeader@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x060000AC RID: 172 RVA: 0x0000404C File Offset: 0x0000224C
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x060000AD RID: 173 RVA: 0x0000405C File Offset: 0x0000225C
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this == null)
			{
				return obj == null;
			}
			global::NPCUA.ListResultsResponse listResultsResponse = obj as global::NPCUA.ListResultsResponse;
			if (listResultsResponse == null)
			{
				return false;
			}
			global::NPCUA.ResponseHeader responseHeader = this.responseHeader@;
			global::NPCUA.ResponseHeader obj2 = listResultsResponse.responseHeader@;
			if (!responseHeader.Equals(obj2, comp))
			{
				return false;
			}
			FSharpList<object> fsharpList = this.results@;
			FSharpList<object> fsharpList2 = listResultsResponse.results@;
			if (fsharpList.Equals(fsharpList2, comp))
			{
				fsharpList = this.diagnosticInfos@;
				fsharpList2 = listResultsResponse.diagnosticInfos@;
				return fsharpList.Equals(fsharpList2, comp);
			}
			return false;
		}

		// Token: 0x060000AE RID: 174 RVA: 0x000040D0 File Offset: 0x000022D0
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.ListResultsResponse obj)
		{
			if (this != null)
			{
				return obj != null && this.responseHeader@.Equals(obj.responseHeader@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpList<object>>(this.results@, obj.results@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpList<object>>(this.diagnosticInfos@, obj.diagnosticInfos@);
			}
			return obj == null;
		}

		// Token: 0x060000AF RID: 175 RVA: 0x0000412C File Offset: 0x0000232C
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.ListResultsResponse listResultsResponse = obj as global::NPCUA.ListResultsResponse;
			return listResultsResponse != null && this.Equals(listResultsResponse);
		}

		// Token: 0x0400002A RID: 42
		[DebuggerBrowsable(0)]
		internal global::NPCUA.ResponseHeader responseHeader@;

		// Token: 0x0400002B RID: 43
		[DebuggerBrowsable(0)]
		internal FSharpList<object> results@;

		// Token: 0x0400002C RID: 44
		[DebuggerBrowsable(0)]
		internal FSharpList<object> diagnosticInfos@;
	}

	// Token: 0x02000012 RID: 18
	[CompilationMapping(2)]
	[Serializable]
	public sealed class DataValue : IEquatable<global::NPCUA.DataValue>, IStructuralEquatable
	{
		// Token: 0x1700002C RID: 44
		// (get) Token: 0x060000B0 RID: 176 RVA: 0x00004150 File Offset: 0x00002350
		[CompilationMapping(4, 0)]
		public FSharpOption<object> value
		{
			get
			{
				return this.value@;
			}
		}

		// Token: 0x1700002D RID: 45
		// (get) Token: 0x060000B1 RID: 177 RVA: 0x00004158 File Offset: 0x00002358
		[CompilationMapping(4, 1)]
		public uint statusCode
		{
			get
			{
				return this.statusCode@;
			}
		}

		// Token: 0x1700002E RID: 46
		// (get) Token: 0x060000B2 RID: 178 RVA: 0x00004160 File Offset: 0x00002360
		[CompilationMapping(4, 2)]
		public long sourceTimestamp
		{
			get
			{
				return this.sourceTimestamp@;
			}
		}

		// Token: 0x1700002F RID: 47
		// (get) Token: 0x060000B3 RID: 179 RVA: 0x00004168 File Offset: 0x00002368
		[CompilationMapping(4, 3)]
		public int sourcePicoseconds
		{
			get
			{
				return this.sourcePicoseconds@;
			}
		}

		// Token: 0x17000030 RID: 48
		// (get) Token: 0x060000B4 RID: 180 RVA: 0x00004170 File Offset: 0x00002370
		[CompilationMapping(4, 4)]
		public long serverTimestamp
		{
			get
			{
				return this.serverTimestamp@;
			}
		}

		// Token: 0x17000031 RID: 49
		// (get) Token: 0x060000B5 RID: 181 RVA: 0x00004178 File Offset: 0x00002378
		[CompilationMapping(4, 5)]
		public int serverPicoseconds
		{
			get
			{
				return this.serverPicoseconds@;
			}
		}

		// Token: 0x17000032 RID: 50
		// (get) Token: 0x060000B6 RID: 182 RVA: 0x00004180 File Offset: 0x00002380
		[CompilationMapping(4, 6)]
		public FSharpOption<string> error
		{
			get
			{
				return this.error@;
			}
		}

		// Token: 0x060000B7 RID: 183 RVA: 0x00004188 File Offset: 0x00002388
		public DataValue(FSharpOption<object> value, uint statusCode, long sourceTimestamp, int sourcePicoseconds, long serverTimestamp, int serverPicoseconds, FSharpOption<string> error)
		{
			this.value@ = value;
			this.statusCode@ = statusCode;
			this.sourceTimestamp@ = sourceTimestamp;
			this.sourcePicoseconds@ = sourcePicoseconds;
			this.serverTimestamp@ = serverTimestamp;
			this.serverPicoseconds@ = serverPicoseconds;
			this.error@ = error;
		}

		// Token: 0x060000B8 RID: 184 RVA: 0x000041C8 File Offset: 0x000023C8
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.DataValue, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.DataValue, string>, Unit, string, string, global::NPCUA.DataValue>("%+A")).Invoke(this);
		}

		// Token: 0x060000B9 RID: 185 RVA: 0x000041E0 File Offset: 0x000023E0
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				return global::NPCUA.GetHashCode$cont@395(comp, this, null);
			}
			return 0;
		}

		// Token: 0x060000BA RID: 186 RVA: 0x000041F0 File Offset: 0x000023F0
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x060000BB RID: 187 RVA: 0x00004200 File Offset: 0x00002400
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.DataValue dataValue = obj as global::NPCUA.DataValue;
				return dataValue != null && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<object>>(comp, this.value@, dataValue.value@) && this.statusCode@ == dataValue.statusCode@ && this.sourceTimestamp@ == dataValue.sourceTimestamp@ && this.sourcePicoseconds@ == dataValue.sourcePicoseconds@ && this.serverTimestamp@ == dataValue.serverTimestamp@ && this.serverPicoseconds@ == dataValue.serverPicoseconds@ && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<string>>(comp, this.error@, dataValue.error@);
			}
			return obj == null;
		}

		// Token: 0x060000BC RID: 188 RVA: 0x000042A4 File Offset: 0x000024A4
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.DataValue obj)
		{
			if (this != null)
			{
				return obj != null && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<object>>(this.value@, obj.value@) && this.statusCode@ == obj.statusCode@ && this.sourceTimestamp@ == obj.sourceTimestamp@ && this.sourcePicoseconds@ == obj.sourcePicoseconds@ && this.serverTimestamp@ == obj.serverTimestamp@ && this.serverPicoseconds@ == obj.serverPicoseconds@ && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<string>>(this.error@, obj.error@);
			}
			return obj == null;
		}

		// Token: 0x060000BD RID: 189 RVA: 0x00004340 File Offset: 0x00002540
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.DataValue dataValue = obj as global::NPCUA.DataValue;
			return dataValue != null && this.Equals(dataValue);
		}

		// Token: 0x0400002D RID: 45
		[DebuggerBrowsable(0)]
		internal FSharpOption<object> value@;

		// Token: 0x0400002E RID: 46
		[DebuggerBrowsable(0)]
		internal uint statusCode@;

		// Token: 0x0400002F RID: 47
		[DebuggerBrowsable(0)]
		internal long sourceTimestamp@;

		// Token: 0x04000030 RID: 48
		[DebuggerBrowsable(0)]
		internal int sourcePicoseconds@;

		// Token: 0x04000031 RID: 49
		[DebuggerBrowsable(0)]
		internal long serverTimestamp@;

		// Token: 0x04000032 RID: 50
		[DebuggerBrowsable(0)]
		internal int serverPicoseconds@;

		// Token: 0x04000033 RID: 51
		[DebuggerBrowsable(0)]
		internal FSharpOption<string> error@;
	}

	// Token: 0x02000013 RID: 19
	[CompilationMapping(2)]
	[Serializable]
	public sealed class StatusCode : IEquatable<global::NPCUA.StatusCode>, IStructuralEquatable, IComparable<global::NPCUA.StatusCode>, IComparable, IStructuralComparable
	{
		// Token: 0x17000033 RID: 51
		// (get) Token: 0x060000BE RID: 190 RVA: 0x00004364 File Offset: 0x00002564
		[CompilationMapping(4, 0)]
		public uint statusCode
		{
			get
			{
				return this.statusCode@;
			}
		}

		// Token: 0x17000034 RID: 52
		// (get) Token: 0x060000BF RID: 191 RVA: 0x0000436C File Offset: 0x0000256C
		[CompilationMapping(4, 1)]
		public FSharpOption<string> error
		{
			get
			{
				return this.error@;
			}
		}

		// Token: 0x060000C0 RID: 192 RVA: 0x00004374 File Offset: 0x00002574
		public StatusCode(uint statusCode, FSharpOption<string> error)
		{
			this.statusCode@ = statusCode;
			this.error@ = error;
		}

		// Token: 0x060000C1 RID: 193 RVA: 0x0000438C File Offset: 0x0000258C
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.StatusCode, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.StatusCode, string>, Unit, string, string, global::NPCUA.StatusCode>("%+A")).Invoke(this);
		}

		// Token: 0x060000C2 RID: 194 RVA: 0x000043A4 File Offset: 0x000025A4
		[CompilerGenerated]
		public sealed int CompareTo(global::NPCUA.StatusCode obj)
		{
			if (this != null)
			{
				if (obj == null)
				{
					return 1;
				}
				IComparer genericComparer = LanguagePrimitives.GenericComparer;
				uint num = this.statusCode@;
				uint num2 = obj.statusCode@;
				int num3 = ((num > num2) - (num < num2)) ? 1 : 0;
				if (num3 < 0)
				{
					return num3;
				}
				if (num3 > 0)
				{
					return num3;
				}
				return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(LanguagePrimitives.GenericComparer, this.error@, obj.error@);
			}
			else
			{
				if (obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x060000C3 RID: 195 RVA: 0x00004404 File Offset: 0x00002604
		[CompilerGenerated]
		public sealed int CompareTo(object obj)
		{
			return this.CompareTo((global::NPCUA.StatusCode)obj);
		}

		// Token: 0x060000C4 RID: 196 RVA: 0x00004414 File Offset: 0x00002614
		[CompilerGenerated]
		public sealed int CompareTo(object obj, IComparer comp)
		{
			global::NPCUA.StatusCode statusCode = (global::NPCUA.StatusCode)obj;
			if (this != null)
			{
				if ((global::NPCUA.StatusCode)obj == null)
				{
					return 1;
				}
				uint num = this.statusCode@;
				uint num2 = statusCode.statusCode@;
				int num3 = ((num > num2) - (num < num2)) ? 1 : 0;
				if (num3 < 0)
				{
					return num3;
				}
				if (num3 > 0)
				{
					return num3;
				}
				return LanguagePrimitives.HashCompare.GenericComparisonWithComparerIntrinsic<FSharpOption<string>>(comp, this.error@, statusCode.error@);
			}
			else
			{
				if ((global::NPCUA.StatusCode)obj != null)
				{
					return -1;
				}
				return 0;
			}
		}

		// Token: 0x060000C5 RID: 197 RVA: 0x0000447C File Offset: 0x0000267C
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<FSharpOption<string>>(comp, this.error@) + ((num << 6) + (num >> 2)));
				return (int)(2654435769U + (this.statusCode@ + (uint)((num << 6) + (num >> 2))));
			}
			return 0;
		}

		// Token: 0x060000C6 RID: 198 RVA: 0x000044C4 File Offset: 0x000026C4
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x060000C7 RID: 199 RVA: 0x000044D4 File Offset: 0x000026D4
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this != null)
			{
				global::NPCUA.StatusCode statusCode = obj as global::NPCUA.StatusCode;
				return statusCode != null && this.statusCode@ == statusCode.statusCode@ && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<FSharpOption<string>>(comp, this.error@, statusCode.error@);
			}
			return obj == null;
		}

		// Token: 0x060000C8 RID: 200 RVA: 0x0000451C File Offset: 0x0000271C
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.StatusCode obj)
		{
			if (this != null)
			{
				return obj != null && this.statusCode@ == obj.statusCode@ && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<FSharpOption<string>>(this.error@, obj.error@);
			}
			return obj == null;
		}

		// Token: 0x060000C9 RID: 201 RVA: 0x00004554 File Offset: 0x00002754
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.StatusCode statusCode = obj as global::NPCUA.StatusCode;
			return statusCode != null && this.Equals(statusCode);
		}

		// Token: 0x04000034 RID: 52
		[DebuggerBrowsable(0)]
		internal uint statusCode@;

		// Token: 0x04000035 RID: 53
		[DebuggerBrowsable(0)]
		internal FSharpOption<string> error@;
	}

	// Token: 0x02000014 RID: 20
	[CompilationMapping(2)]
	[Serializable]
	public sealed class ErrorResponse : IEquatable<global::NPCUA.ErrorResponse>, IStructuralEquatable
	{
		// Token: 0x17000035 RID: 53
		// (get) Token: 0x060000CA RID: 202 RVA: 0x00004578 File Offset: 0x00002778
		[CompilationMapping(4, 0)]
		public global::NPCUA.ResponseHeader responseHeader
		{
			get
			{
				return this.responseHeader@;
			}
		}

		// Token: 0x17000036 RID: 54
		// (get) Token: 0x060000CB RID: 203 RVA: 0x00004580 File Offset: 0x00002780
		[CompilationMapping(4, 1)]
		public string error
		{
			get
			{
				return this.error@;
			}
		}

		// Token: 0x17000037 RID: 55
		// (get) Token: 0x060000CC RID: 204 RVA: 0x00004588 File Offset: 0x00002788
		[CompilationMapping(4, 2)]
		public object[] diagnosticInfos
		{
			get
			{
				return this.diagnosticInfos@;
			}
		}

		// Token: 0x060000CD RID: 205 RVA: 0x00004590 File Offset: 0x00002790
		public ErrorResponse(global::NPCUA.ResponseHeader responseHeader, string error, object[] diagnosticInfos)
		{
			this.responseHeader@ = responseHeader;
			this.error@ = error;
			this.diagnosticInfos@ = diagnosticInfos;
		}

		// Token: 0x060000CE RID: 206 RVA: 0x000045B0 File Offset: 0x000027B0
		[CompilerGenerated]
		public override string ToString()
		{
			return ExtraTopLevelOperators.PrintFormatToString<FSharpFunc<global::NPCUA.ErrorResponse, string>>(new PrintfFormat<FSharpFunc<global::NPCUA.ErrorResponse, string>, Unit, string, string, global::NPCUA.ErrorResponse>("%+A")).Invoke(this);
		}

		// Token: 0x060000CF RID: 207 RVA: 0x000045C8 File Offset: 0x000027C8
		[CompilerGenerated]
		public sealed int GetHashCode(IEqualityComparer comp)
		{
			if (this != null)
			{
				int num = 0;
				num = -1640531527 + (LanguagePrimitives.HashCompare.GenericHashWithComparerIntrinsic<object[]>(comp, this.diagnosticInfos@) + ((num << 6) + (num >> 2)));
				int num2 = -1640531527;
				string text = this.error@;
				num = num2 + (((text != null) ? text.GetHashCode() : 0) + ((num << 6) + (num >> 2)));
				return -1640531527 + (this.responseHeader@.GetHashCode(comp) + ((num << 6) + (num >> 2)));
			}
			return 0;
		}

		// Token: 0x060000D0 RID: 208 RVA: 0x00004638 File Offset: 0x00002838
		[CompilerGenerated]
		public sealed override int GetHashCode()
		{
			return this.GetHashCode(LanguagePrimitives.GenericEqualityComparer);
		}

		// Token: 0x060000D1 RID: 209 RVA: 0x00004648 File Offset: 0x00002848
		[CompilerGenerated]
		public sealed bool Equals(object obj, IEqualityComparer comp)
		{
			if (this == null)
			{
				return obj == null;
			}
			global::NPCUA.ErrorResponse errorResponse = obj as global::NPCUA.ErrorResponse;
			if (errorResponse != null)
			{
				global::NPCUA.ResponseHeader responseHeader = this.responseHeader@;
				global::NPCUA.ResponseHeader obj2 = errorResponse.responseHeader@;
				return responseHeader.Equals(obj2, comp) && string.Equals(this.error@, errorResponse.error@) && LanguagePrimitives.HashCompare.GenericEqualityWithComparerIntrinsic<object[]>(comp, this.diagnosticInfos@, errorResponse.diagnosticInfos@);
			}
			return false;
		}

		// Token: 0x060000D2 RID: 210 RVA: 0x000046B0 File Offset: 0x000028B0
		[CompilerGenerated]
		public sealed override bool Equals(global::NPCUA.ErrorResponse obj)
		{
			if (this != null)
			{
				return obj != null && this.responseHeader@.Equals(obj.responseHeader@) && string.Equals(this.error@, obj.error@) && LanguagePrimitives.HashCompare.GenericEqualityERIntrinsic<object[]>(this.diagnosticInfos@, obj.diagnosticInfos@);
			}
			return obj == null;
		}

		// Token: 0x060000D3 RID: 211 RVA: 0x0000470C File Offset: 0x0000290C
		[CompilerGenerated]
		public sealed override bool Equals(object obj)
		{
			global::NPCUA.ErrorResponse errorResponse = obj as global::NPCUA.ErrorResponse;
			return errorResponse != null && this.Equals(errorResponse);
		}

		// Token: 0x04000036 RID: 54
		[DebuggerBrowsable(0)]
		internal global::NPCUA.ResponseHeader responseHeader@;

		// Token: 0x04000037 RID: 55
		[DebuggerBrowsable(0)]
		internal string error@;

		// Token: 0x04000038 RID: 56
		[DebuggerBrowsable(0)]
		internal object[] diagnosticInfos@;
	}

	// Token: 0x02000015 RID: 21
	[CompilationMapping(3)]
	[Serializable]
	public class CryptoSystem
	{
		// Token: 0x060000D4 RID: 212 RVA: 0x00004730 File Offset: 0x00002930
		public CryptoSystem(FSharpFunc<Unit, Unit> loadPublicKey, FSharpFunc<Unit, Crypto> loadPrivateKey) : this()
		{
			this.privateKey = loadPrivateKey.Invoke(null);
			loadPublicKey.Invoke(null);
		}

		// Token: 0x060000D5 RID: 213 RVA: 0x00004750 File Offset: 0x00002950
		public bool VerifyString(string data, string signature)
		{
			return this.privateKey.VerifyString(data, signature);
		}

		// Token: 0x060000D6 RID: 214 RVA: 0x00004760 File Offset: 0x00002960
		public string SignString(string data)
		{
			return this.privateKey.SignString(data);
		}

		// Token: 0x04000039 RID: 57
		internal Crypto privateKey;
	}

	// Token: 0x02000016 RID: 22
	[Serializable]
	internal sealed class loadPublicKey@435 : FSharpFunc<Unit, Unit>
	{
		// Token: 0x060000D7 RID: 215 RVA: 0x00004770 File Offset: 0x00002970
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal loadPublicKey@435(string pub_key_path)
		{
			this.pub_key_path = pub_key_path;
		}

		// Token: 0x060000D8 RID: 216 RVA: 0x00004780 File Offset: 0x00002980
		public override Unit Invoke(Unit unitVar0)
		{
			global::NPCUA.application_pubkey = File.ReadAllBytes(this.pub_key_path);
			return null;
		}

		// Token: 0x0400003A RID: 58
		public string pub_key_path;
	}

	// Token: 0x02000017 RID: 23
	[Serializable]
	internal sealed class loadPrivateKey@437 : FSharpFunc<Unit, Crypto>
	{
		// Token: 0x060000D9 RID: 217 RVA: 0x00004794 File Offset: 0x00002994
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal loadPrivateKey@437(string priv_key_path)
		{
			this.priv_key_path = priv_key_path;
		}

		// Token: 0x060000DA RID: 218 RVA: 0x000047A4 File Offset: 0x000029A4
		public override Crypto Invoke(Unit unitVar0)
		{
			return new Crypto(this.priv_key_path);
		}

		// Token: 0x0400003B RID: 59
		public string priv_key_path;
	}

	// Token: 0x02000018 RID: 24
	[CompilationMapping(3)]
	[Serializable]
	public class NPCUA
	{
		// Token: 0x060000DB RID: 219 RVA: 0x000047B4 File Offset: 0x000029B4
		public NPCUA(Stream inputIn, Stream outputIn) : this()
		{
			this.input = inputIn;
			this.output = outputIn;
			this.status_codes = global::NPCUA.loadStatusCodes("StatusCode.csv");
			this.crypto = global::NPCUA.GetCryptoSystem(".");
			this.foo = "";
			this.send_sec = false;
		}

		// Token: 0x060000DC RID: 220 RVA: 0x0000480C File Offset: 0x00002A0C
		public void start_connection()
		{
			for (;;)
			{
				this.read_msg();
			}
		}

		// Token: 0x060000DD RID: 221 RVA: 0x0000481C File Offset: 0x00002A1C
		public void send_msg(string name, global::NPCUA.BitWriter bw)
		{
			global::NPCUA.BitWriter bitWriter = new global::NPCUA.BitWriter(Array.Empty<byte>())
			{
				post_data = bw.data()
			};
			bitWriter.append(Encoding.ASCII.GetBytes(name));
			bitWriter.append(new byte[]
			{
				0
			});
			int num = bw.data().Length + 8;
			bitWriter.append(BitConverter.GetBytes(num));
			this.output.Write(bitWriter.data(), 0, bitWriter.data().Length);
		}

		// Token: 0x060000DE RID: 222 RVA: 0x000048A0 File Offset: 0x00002AA0
		public void send_sec_msg(string name, global::NPCUA.BitWriter bw)
		{
			int num = 0;
			string s = "http://nautilus.npc/UA/SecurityPolicy#None";
			if (this.send_sec)
			{
				num = 1;
				s = "http://nautilus.npc/UA/SecurityPolicy#Basic256Sha256";
			}
			global::NPCUA.BitWriter bitWriter = new global::NPCUA.BitWriter(Array.Empty<byte>())
			{
				post_data = bw.data()
			};
			int num2 = num;
			bitWriter.append(BitConverter.GetBytes(num2));
			bitWriter.str(s);
			bitWriter.byte_array(global::NPCUA.application_pubkey);
			bitWriter.append(BitConverter.GetBytes(0));
			bitWriter.append(BitConverter.GetBytes(0));
			bitWriter.append(BitConverter.GetBytes(0));
			this.send_msg(name, bitWriter);
		}

		// Token: 0x060000DF RID: 223 RVA: 0x0000493C File Offset: 0x00002B3C
		public Tuple<uint, string, byte[], uint, uint, uint> read_sec_msg_header(global::NPCUA.BitReader br)
		{
			uint item = BitConverter.ToUInt32(br.bytes(4), 0);
			uint length = BitConverter.ToUInt32(br.bytes(4), 0);
			byte[] array = br.bytes((int)length);
			string @string = Encoding.UTF8.GetString(array);
			length = BitConverter.ToUInt32(br.bytes(4), 0);
			return new Tuple<uint, string, byte[], uint, uint, uint>(item, @string, br.bytes((int)length), BitConverter.ToUInt32(br.bytes(4), 0), BitConverter.ToUInt32(br.bytes(4), 0), BitConverter.ToUInt32(br.bytes(4), 0));
		}

		// Token: 0x060000E0 RID: 224 RVA: 0x000049B8 File Offset: 0x00002BB8
		public void send_ack()
		{
			global::NPCUA.BitWriter bitWriter = new global::NPCUA.BitWriter(Array.Empty<byte>());
			bitWriter.append(BitConverter.GetBytes(1337));
			bitWriter.append(BitConverter.GetBytes(4096));
			bitWriter.append(BitConverter.GetBytes(4096));
			bitWriter.append(BitConverter.GetBytes(4096));
			bitWriter.append(BitConverter.GetBytes(1));
			this.send_msg("ACK", bitWriter);
		}

		// Token: 0x060000E1 RID: 225 RVA: 0x00004A30 File Offset: 0x00002C30
		public int get_status_code(string name)
		{
			return MapModule.Find<string, Tuple<int, string>>(name, this.status_codes).Item1;
		}

		// Token: 0x060000E2 RID: 226 RVA: 0x00004A44 File Offset: 0x00002C44
		public string get_status_message(string name)
		{
			return MapModule.Find<string, Tuple<int, string>>(name, this.status_codes).Item2;
		}

		// Token: 0x060000E3 RID: 227 RVA: 0x00004A58 File Offset: 0x00002C58
		public void send_err(string name)
		{
			Tuple<int, string> tuple = MapModule.Find<string, Tuple<int, string>>(name, this.status_codes);
			int item = tuple.Item1;
			string item2 = tuple.Item2;
			global::NPCUA.BitWriter bitWriter = new global::NPCUA.BitWriter(Array.Empty<byte>());
			bitWriter.append(BitConverter.GetBytes(item));
			bitWriter.str(item2);
			this.send_msg("ERR", bitWriter);
		}

		// Token: 0x060000E4 RID: 228 RVA: 0x00004AB0 File Offset: 0x00002CB0
		public void handle_hello(global::NPCUA.BitReader br)
		{
			uint num = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num2 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num3 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num4 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num5 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint length = BitConverter.ToUInt32(br.bytes(4), 0);
			byte[] array = br.bytes((int)length);
			string @string = Encoding.UTF8.GetString(array);
			this.send_ack();
		}

		// Token: 0x060000E5 RID: 229 RVA: 0x00004B34 File Offset: 0x00002D34
		public void send_service_response(object res)
		{
			string text = Json.serializeEx(global::NPCUA._JsonConfig, res);
			global::NPCUA.BitWriter bitWriter = new global::NPCUA.BitWriter(Array.Empty<byte>());
			byte[] bytes = Encoding.UTF8.GetBytes(text);
			bitWriter.append(bytes);
			this.send_sec_msg("MSG", bitWriter);
		}

		// Token: 0x060000E6 RID: 230 RVA: 0x00004B7C File Offset: 0x00002D7C
		public void send_service_err(string name, FSharpOption<global::NPCUA.RequestHeader> req)
		{
			Tuple<int, string> tuple = MapModule.Find<string, Tuple<int, string>>(name, this.status_codes);
			string item = tuple.Item2;
			this.send_service_response(new global::NPCUA.ErrorResponse(this.make_response_header(name, req), item, Array.Empty<object>()));
		}

		// Token: 0x060000E7 RID: 231 RVA: 0x00004BB8 File Offset: 0x00002DB8
		public void handle_msg(global::NPCUA.BitReader br)
		{
			Tuple<uint, string, byte[], uint, uint, uint> tuple = this.read_sec_msg_header(br);
			uint num = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num2 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num3 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint num4 = BitConverter.ToUInt32(br.bytes(4), 0);
			uint service_id = BitConverter.ToUInt32(br.bytes(4), 0);
			this.handle_service_request(br, service_id);
		}

		// Token: 0x060000E8 RID: 232 RVA: 0x00004C20 File Offset: 0x00002E20
		public void handle_service_request(global::NPCUA.BitReader br, uint service_id)
		{
			FSharpOption<FSharpMap<string, object>> fsharpOption = this.get_json_request(br);
			if (fsharpOption == null)
			{
				this.send_service_err("BadDecodingError", null);
				return;
			}
			FSharpMap<string, object> value = fsharpOption.Value;
			FSharpOption<global::NPCUA.RequestHeader> fsharpOption2 = this.get_service_request_header(value);
			if (fsharpOption2 == null)
			{
				this.send_service_err("BadInvalidArgument", null);
				return;
			}
			global::NPCUA.RequestHeader value2 = fsharpOption2.Value;
			switch (service_id)
			{
			case 629U:
				this.handle_read_service(value, value2);
				return;
			case 630U:
				this.handle_write_service(value, value2);
				return;
			case 631U:
				this.handle_export_service(value, value2);
				return;
			case 632U:
				this.handle_import_service(value, value2);
				return;
			default:
				this.send_err("BadServiceUnsupported");
				return;
			}
		}

		// Token: 0x060000E9 RID: 233 RVA: 0x00004CCC File Offset: 0x00002ECC
		public global::NPCUA.ResponseHeader make_response_header(string status, FSharpOption<global::NPCUA.RequestHeader> reqh)
		{
			return new global::NPCUA.ResponseHeader(DateTime.Now.ToFileTimeUtc(), (reqh == null) ? 0 : reqh.Value.requestHandle@, (uint)MapModule.Find<string, Tuple<int, string>>(status, this.status_codes).Item1, null, Array.Empty<string>());
		}

		// Token: 0x060000EA RID: 234 RVA: 0x00004D18 File Offset: 0x00002F18
		public FSharpOption<global::NPCUA.RequestHeader> get_service_request_header(FSharpMap<string, object> json)
		{
			FSharpOption<FSharpMap<string, object>> fsharpOption = global::NPCUA.tryFindMapValueAsType<FSharpMap<string, object>>(json, "requestHeader");
			if (LanguagePrimitives.HashCompare.GenericEqualityIntrinsic<FSharpOption<FSharpMap<string, object>>>(fsharpOption, null))
			{
				return null;
			}
			FSharpMap<string, object> value = fsharpOption.Value;
			return FSharpOption<global::NPCUA.RequestHeader>.Some(new global::NPCUA.RequestHeader(global::NPCUA.tryFindMapValueAsType<string>(value, "authToken"), (long)global::NPCUA.tryFindMapValueAsTypeDefault<decimal>(value, "timestamp", Convert.ToDecimal(0)), (int)global::NPCUA.tryFindMapValueAsTypeDefault<decimal>(value, "requestHandle", Convert.ToDecimal(0)), global::NPCUA.int32Option(global::NPCUA.tryFindMapValueAsType<decimal>(value, "returnDiagnostics")), global::NPCUA.tryFindMapValueAsType<string>(value, "auditEntryId"), global::NPCUA.int32Option(global::NPCUA.tryFindMapValueAsType<decimal>(value, "timeoutHint"))));
		}

		// Token: 0x060000EB RID: 235 RVA: 0x00004DB0 File Offset: 0x00002FB0
		public FSharpOption<FSharpMap<string, object>> get_json_request(global::NPCUA.BitReader br)
		{
			FSharpOption<string> fsharpOption;
			try
			{
				byte[] array = br.rest();
				fsharpOption = FSharpOption<string>.Some(Encoding.UTF8.GetString(array));
			}
			catch (object obj)
			{
				Exception ex = (Exception)obj;
				fsharpOption = null;
			}
			FSharpOption<string> fsharpOption2 = fsharpOption;
			if (fsharpOption2 != null)
			{
				FSharpOption<FSharpMap<string, object>> result;
				try
				{
					result = FSharpOption<FSharpMap<string, object>>.Some(Json.deserializeEx<FSharpMap<string, object>>(global::NPCUA._JsonConfig, fsharpOption2.Value));
				}
				catch (object obj2)
				{
					Exception ex = (Exception)obj2;
					result = null;
				}
				return result;
			}
			return null;
		}

		// Token: 0x060000EC RID: 236 RVA: 0x00004E30 File Offset: 0x00003030
		public void handle_import_service(FSharpMap<string, object> json, global::NPCUA.RequestHeader reqh)
		{
			FSharpOption<FSharpList<object>> fsharpOption = global::NPCUA.tryFindMapValueAsType<FSharpList<object>>(json, "nodesToImport");
			if (fsharpOption == null)
			{
				this.send_service_err("BadInvalidArgument", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
				return;
			}
			FSharpList<object> value = fsharpOption.Value;
			FSharpList<object> fsharpList = ListModule.Map<object, object>(new global::NPCUA.res@666(this), value);
			this.send_service_err("Good", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
		}

		// Token: 0x060000ED RID: 237 RVA: 0x00004E88 File Offset: 0x00003088
		public void handle_export_service(FSharpMap<string, object> json, global::NPCUA.RequestHeader reqh)
		{
			FSharpOption<FSharpList<object>> fsharpOption = global::NPCUA.tryFindMapValueAsType<FSharpList<object>>(json, "nodesToExport");
			if (fsharpOption == null)
			{
				this.send_service_err("BadInvalidArgument", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
				return;
			}
			FSharpList<object> value = fsharpOption.Value;
			FSharpList<object> results = ListModule.Map<object, object>(new global::NPCUA.res@717-1(this), value);
			this.send_service_response(new global::NPCUA.ListResultsResponse(this.make_response_header("Good", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh)), results, FSharpList<object>.Empty));
		}

		// Token: 0x060000EE RID: 238 RVA: 0x00004EF4 File Offset: 0x000030F4
		public void handle_write_service(FSharpMap<string, object> json, global::NPCUA.RequestHeader reqh)
		{
			FSharpOption<FSharpList<object>> fsharpOption = global::NPCUA.tryFindMapValueAsType<FSharpList<object>>(json, "nodesToWrite");
			if (fsharpOption == null)
			{
				this.send_service_err("BadInvalidArgument", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
				return;
			}
			FSharpList<object> value = fsharpOption.Value;
			if (value.Length == 0)
			{
				this.send_service_err("BadNothingToDo", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
				return;
			}
			FSharpList<object> results = ListModule.Map<object, object>(new global::NPCUA.res@784-2(this), value);
			this.send_service_response(new global::NPCUA.ListResultsResponse(this.make_response_header("Good", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh)), results, FSharpList<object>.Empty));
		}

		// Token: 0x060000EF RID: 239 RVA: 0x00004F7C File Offset: 0x0000317C
		public void handle_read_service(FSharpMap<string, object> json, global::NPCUA.RequestHeader reqh)
		{
			FSharpOption<FSharpList<object>> fsharpOption = global::NPCUA.tryFindMapValueAsType<FSharpList<object>>(json, "nodesToRead");
			if (fsharpOption == null)
			{
				this.send_service_err("BadInvalidArgument", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh));
				return;
			}
			FSharpList<object> value = fsharpOption.Value;
			if (value.Length == 0)
			{
				this.send_service_response(new global::NPCUA.ListResultsResponse(this.make_response_header("Good", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh)), FSharpList<object>.Empty, FSharpList<object>.Empty));
				return;
			}
			FSharpList<object> results = ListModule.Map<object, object>(new global::NPCUA.res@862-3(this), value);
			this.send_service_response(new global::NPCUA.ListResultsResponse(this.make_response_header("Good", FSharpOption<global::NPCUA.RequestHeader>.Some(reqh)), results, FSharpList<object>.Empty));
		}

		// Token: 0x060000F0 RID: 240 RVA: 0x00005018 File Offset: 0x00003218
		public int read_u32()
		{
			byte[] array = ArrayModule.ZeroCreate<byte>(4);
			int num = this.input.Read(array, 0, 4);
			return BitConverter.ToInt32(array, 0);
		}

		// Token: 0x060000F1 RID: 241 RVA: 0x00005044 File Offset: 0x00003244
		public byte[] read_bytes(int length)
		{
			byte[] array = ArrayModule.ZeroCreate<byte>(length);
			int num = this.input.Read(array, 0, length);
			return array;
		}

		// Token: 0x060000F2 RID: 242 RVA: 0x00005068 File Offset: 0x00003268
		public void read_msg()
		{
			byte[] array = this.read_bytes(4);
			uint num = BitConverter.ToUInt32(this.read_bytes(4), 0);
			byte[] data = this.read_bytes((int)(num - 8U));
			global::NPCUA.BitReader br = new global::NPCUA.BitReader(data);
			string @string = Encoding.ASCII.GetString(array, 0, 3);
			if (string.Equals(@string, "HEL"))
			{
				this.handle_hello(br);
				return;
			}
			if (string.Equals(@string, "MSG"))
			{
				this.handle_msg(br);
				return;
			}
			this.send_err("BadServiceUnsupported");
		}

		// Token: 0x060000F3 RID: 243 RVA: 0x000050EC File Offset: 0x000032EC
		public object get_system_property(string path)
		{
			string[] array = path.Split("/", StringSplitOptions.None);
			string text = array[0];
			string text2 = array[1];
			string name = array[2];
			Assembly assembly = Assembly.Load(text);
			Type type = assembly.GetType(text2, false, false);
			return type.GetProperty(name).GetValue(null, null);
		}

		// Token: 0x0400003C RID: 60
		internal Stream input;

		// Token: 0x0400003D RID: 61
		internal Stream output;

		// Token: 0x0400003E RID: 62
		internal FSharpMap<string, Tuple<int, string>> status_codes;

		// Token: 0x0400003F RID: 63
		internal global::NPCUA.CryptoSystem crypto;

		// Token: 0x04000040 RID: 64
		internal string foo;

		// Token: 0x04000041 RID: 65
		internal bool send_sec;
	}

	// Token: 0x02000019 RID: 25
	[Serializable]
	internal sealed class res@666 : FSharpFunc<object, object>
	{
		// Token: 0x060000F4 RID: 244 RVA: 0x00005144 File Offset: 0x00003344
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal res@666(global::NPCUA.NPCUA @this)
		{
			this.@this = @this;
		}

		// Token: 0x060000F5 RID: 245 RVA: 0x00005154 File Offset: 0x00003354
		public override object Invoke(object json)
		{
			if (json is FSharpMap<string, object>)
			{
				FSharpMap<string, object> map = LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<FSharpMap<string, object>>(json);
				FSharpOption<string> fsharpOption = global::NPCUA.tryFindMapValueAsType<string>(map, "data");
				FSharpOption<string> fsharpOption2 = global::NPCUA.tryFindMapValueAsType<string>(map, "signature");
				if (fsharpOption != null)
				{
					if (fsharpOption2 != null)
					{
						string value = fsharpOption.Value;
						string value2 = fsharpOption2.Value;
						global::NPCUA.CryptoSystem crypto = this.@this.crypto;
						if (!crypto.privateKey.VerifyString(value, value2))
						{
							return global::NPCUA.make_res@667(this.@this, "BadUserSignatureInvalid");
						}
						object obj = global::NPCUA._JsonSerializer.UnPickleOfString<object>(value, null, null);
						if (obj is FSharpFunc<Unit, Unit>)
						{
							LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<FSharpFunc<Unit, Unit>>(obj).Invoke(null);
							return global::NPCUA.make_res@667(this.@this, "Good");
						}
						if (obj is global::NPCUA.VariableNode)
						{
							global::NPCUA.VariableNode variableNode = LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<global::NPCUA.VariableNode>(obj);
							variableNode.Install();
							return global::NPCUA.make_res@667(this.@this, "Good");
						}
						return global::NPCUA.make_res@667(this.@this, "BadNotExecutable");
					}
				}
				return global::NPCUA.make_res@667(this.@this, "BadInvalidArgument");
			}
			return global::NPCUA.make_res@667(this.@this, "BadInvalidArgument");
		}

		// Token: 0x04000042 RID: 66
		public global::NPCUA.NPCUA @this;
	}

	// Token: 0x0200001A RID: 26
	[Serializable]
	internal sealed class res@717-1 : FSharpFunc<object, object>
	{
		// Token: 0x060000F6 RID: 246 RVA: 0x00005270 File Offset: 0x00003470
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal res@717-1(global::NPCUA.NPCUA @this)
		{
			this.@this = @this;
		}

		// Token: 0x060000F7 RID: 247 RVA: 0x00005280 File Offset: 0x00003480
		public override object Invoke(object json)
		{
			if (!(json is FSharpMap<string, object>))
			{
				return global::NPCUA.make_res@718-1(this.@this, "BadInvalidArgument", null);
			}
			FSharpMap<string, object> map = LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<FSharpMap<string, object>>(json);
			FSharpOption<string> fsharpOption = global::NPCUA.tryFindMapValueAsType<string>(map, "nodeId");
			if (fsharpOption == null)
			{
				return global::NPCUA.make_res@718-1(this.@this, "BadNodeIdInvalid", null);
			}
			string value = fsharpOption.Value;
			FSharpOption<global::NPCUA.Node> fsharpOption2 = global::NPCUA.NodeManager.Find(value);
			if (fsharpOption2 == null)
			{
				return global::NPCUA.make_res@718-1(this.@this, "BadNodeIdUnknown", null);
			}
			global::NPCUA.Node value2 = fsharpOption2.Value;
			string data = value2.Serialize();
			global::NPCUA.CryptoSystem crypto = this.@this.crypto;
			string text = crypto.privateKey.SignString(data);
			crypto = this.@this.crypto;
			bool flag = crypto.privateKey.VerifyString(data, text);
			global::NPCUA.SignedData signedData = new global::NPCUA.SignedData(data, text);
			object obj = signedData;
			return global::NPCUA.make_res@718-1(this.@this, "Good", FSharpOption<object>.Some(obj));
		}

		// Token: 0x04000043 RID: 67
		public global::NPCUA.NPCUA @this;
	}

	// Token: 0x0200001B RID: 27
	[Serializable]
	internal sealed class res@784-2 : FSharpFunc<object, object>
	{
		// Token: 0x060000F8 RID: 248 RVA: 0x0000536C File Offset: 0x0000356C
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal res@784-2(global::NPCUA.NPCUA @this)
		{
			this.@this = @this;
		}

		// Token: 0x060000F9 RID: 249 RVA: 0x0000537C File Offset: 0x0000357C
		public override object Invoke(object json)
		{
			if (!(json is FSharpMap<string, object>))
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadInvalidArgument", null);
			}
			FSharpMap<string, object> fsharpMap = LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<FSharpMap<string, object>>(json);
			FSharpOption<string> fsharpOption = global::NPCUA.tryFindMapValueAsType<string>(fsharpMap, "nodeId");
			if (fsharpOption == null)
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadNodeIdInvalid", null);
			}
			string value = fsharpOption.Value;
			FSharpOption<global::NPCUA.Node> fsharpOption2 = global::NPCUA.NodeManager.Find(value);
			if (fsharpOption2 == null)
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadNodeIdUnknown", null);
			}
			global::NPCUA.Node value2 = fsharpOption2.Value;
			FSharpOption<decimal> fsharpOption3 = global::NPCUA.tryFindMapValueAsType<decimal>(fsharpMap, "attributeId");
			if (fsharpOption3 == null)
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadAttributeIdInvalid", null);
			}
			global::NPCUA.AttributeId attributeId = (global::NPCUA.AttributeId)((int)fsharpOption3.Value);
			FSharpOption<object> fsharpOption4 = fsharpMap.TryFind("value");
			if (fsharpOption4 == null)
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadInvalidArgument", null);
			}
			object value3 = fsharpOption4.Value;
			FSharpList<global::NPCUA.AttributeId> allowed_attributes = value2.Allowed_attributes;
			if (!global::NPCUA.contains@1<global::NPCUA.AttributeId>(attributeId, allowed_attributes))
			{
				return global::NPCUA.make_res@785-2<FSharpOption<object>>(this.@this, "BadNodeAttributesInvalid", null);
			}
			if (value2.Write_attribute(attributeId, value3))
			{
				return global::NPCUA.make_res@785-2<object>(this.@this, "Good", value3);
			}
			return global::NPCUA.make_res@785-2<object>(this.@this, "BadAttributeIdInvalid", value3);
		}

		// Token: 0x04000044 RID: 68
		public global::NPCUA.NPCUA @this;
	}

	// Token: 0x0200001C RID: 28
	[Serializable]
	internal sealed class res@862-3 : FSharpFunc<object, object>
	{
		// Token: 0x060000FA RID: 250 RVA: 0x000054B4 File Offset: 0x000036B4
		[CompilerGenerated]
		[DebuggerNonUserCode]
		internal res@862-3(global::NPCUA.NPCUA @this)
		{
			this.@this = @this;
		}

		// Token: 0x060000FB RID: 251 RVA: 0x000054C4 File Offset: 0x000036C4
		public override object Invoke(object json)
		{
			if (!(json is FSharpMap<string, object>))
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadInvalidArgument", null);
			}
			FSharpMap<string, object> map = LanguagePrimitives.IntrinsicFunctions.UnboxGeneric<FSharpMap<string, object>>(json);
			FSharpOption<string> fsharpOption = global::NPCUA.tryFindMapValueAsType<string>(map, "nodeId");
			if (fsharpOption == null)
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadNodeIdInvalid", null);
			}
			string value = fsharpOption.Value;
			FSharpOption<global::NPCUA.Node> fsharpOption2 = global::NPCUA.NodeManager.Find(value);
			if (fsharpOption2 == null)
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadNodeIdUnknown", null);
			}
			global::NPCUA.Node value2 = fsharpOption2.Value;
			FSharpOption<decimal> fsharpOption3 = global::NPCUA.tryFindMapValueAsType<decimal>(map, "attributeId");
			if (fsharpOption3 == null)
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadAttributeIdInvalid", null);
			}
			global::NPCUA.AttributeId attributeId = (global::NPCUA.AttributeId)((int)fsharpOption3.Value);
			FSharpList<global::NPCUA.AttributeId> allowed_attributes = value2.Allowed_attributes;
			if (!global::NPCUA.contains@1-1<global::NPCUA.AttributeId>(attributeId, allowed_attributes))
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadNodeAttributesInvalid", null);
			}
			FSharpOption<object> fsharpOption4 = value2.Read_attribute(attributeId);
			if (fsharpOption4 == null)
			{
				return global::NPCUA.make_res@863-3(this.@this, "BadAttributeIdInvalid", fsharpOption4);
			}
			object value3 = fsharpOption4.Value;
			if (value3 is string)
			{
				string str = (string)value3;
				string data = "\"" + str + "\"";
				global::NPCUA.CryptoSystem crypto = this.@this.crypto;
				string text = crypto.privateKey.SignString(data);
				crypto = this.@this.crypto;
				bool flag = crypto.privateKey.VerifyString(data, text);
				global::NPCUA.SignedData signedData = new global::NPCUA.SignedData(data, text);
				object obj = signedData;
				return global::NPCUA.make_res@863-3(this.@this, "Good", FSharpOption<object>.Some(obj));
			}
			return global::NPCUA.make_res@863-3(this.@this, "Good", FSharpOption<object>.Some(value3));
		}

		// Token: 0x04000045 RID: 69
		public global::NPCUA.NPCUA @this;
	}
}
