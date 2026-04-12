import json, os
out = "src/main/resources/crimsonEyedResources/localization/jpn"
os.makedirs(out, exist_ok=True)

cards = {}

cards["crimsonEyed:AbsorbChakra"] = {"NAME":"チャクラ吸収","DESCRIPTION":"!M! HPを回復する。 NL [E]を得る。 NL 廃棄する。","UPGRADE_DESCRIPTION":"!M! HPを回復する。 NL [E][E]を得る。 NL 廃棄する。"}
cards["crimsonEyed:Agonize"] = {"NAME":"苦悶","DESCRIPTION":"状態異常またはカースカードを引くたびに、筋力を1得る。"}
cards["crimsonEyed:AlmightyPush"] = {"NAME":"万象斥力","DESCRIPTION":"手札を全て捨てる。 NL 捨てたカードの枚数の!M!倍のダメージを全ての敵に与える。"}
cards["crimsonEyed:Amaterasu"] = {"NAME":"天照","DESCRIPTION":"!M! HPを失う。 NL !D! ダメージを与える。 NL ダーク1つを生成する。"}
cards["crimsonEyed:Amenotejikara"] = {"NAME":"天手力","DESCRIPTION":"山札から攻撃カードを!M!枚手札に加える。 NL このカードを山札に混ぜる。","UPGRADE_DESCRIPTION":"山札から攻撃カードを!M!枚手札に加える。 NL このカードを山札に混ぜる。"}
cards["crimsonEyed:AmpUp"] = {"NAME":"増幅","DESCRIPTION":"生成中のオーブ1つにつき[E]を得る。"}
cards["crimsonEyed:Analyze"] = {"NAME":"分析","DESCRIPTION":"!B! ブロックを得る。 NL 集中力がこのカードに!M!回効果を与える。"}
cards["crimsonEyed:Anticipate"] = {"NAME":"読み","DESCRIPTION":"!B! ブロックを得る。 NL 選択: NL 次のターン、カードを!M!枚引く NL または[E]を得る。","UPGRADE_DESCRIPTION":"!B! ブロックを得る。 NL 選択: NL 次のターン、カードを!M!枚引く、[E]を得る、または!B! ブロックを得る。"}
cards["crimsonEyed:BoneBreaker"] = {"NAME":"骨砕き","DESCRIPTION":"!D! ダメージを与える。 NL 金属化を!M!得る。"}
cards["crimsonEyed:BlazeBarrier2"] = {"NAME":"炎壁","DESCRIPTION":"ダーク1つを生成する。 NL 次のオーブの解放量と等しいブロックを得る。","UPGRADE_DESCRIPTION":"ダーク1つを生成する。 NL 次のオーブのパッシブ効果を発動し、その解放量と等しいブロックを得る。"}
cards["crimsonEyed:Chidori"] = {"NAME":"千鳥","DESCRIPTION":"!D! ダメージを与える。 NL ライトニング1つを生成する。 NL 敵がロックオン状態なら、次のオーブを解放する。"}
cards["crimsonEyed:ChidoriBlade"] = {"NAME":"千鳥・刀","DESCRIPTION":"!D! ダメージを与える。 NL 次のオーブのパッシブ効果を発動する。"}
cards["crimsonEyed:ChidoriSenbon"] = {"NAME":"千鳥千本","DESCRIPTION":"全ての敵に!D! ダメージを与える。 NL ライトニング1つを生成する。"}
cards["crimsonEyed:ChidoriSpear"] = {"NAME":"千鳥鋭槍","DESCRIPTION":"!D! ダメージを与える。 NL ライトニング2つを生成する。"}
cards["crimsonEyed:ChidoriStream"] = {"NAME":"千鳥流し","DESCRIPTION":"集中力を!M!得る。 NL このターン終了時、集中力を!M!失う。 NL ライトニング1つを生成する。"}
cards["crimsonEyed:Chop2"] = {"NAME":"斬り","DESCRIPTION":"選択: !D! ダメージを与えるか、全ての敵に!M! ダメージを与える。","UPGRADE_DESCRIPTION":"選択: !D! ダメージを与えるか、全ての敵に!M! ダメージを与える。","EXTENDED_DESCRIPTION":["選択: !D! ダメージを与える、全ての敵に!M! ダメージを与える、またはランダムな敵に!crimsonEyed:M2! ダメージを5回与える。","選択: !D! ダメージを与える、全ての敵に!M! ダメージを与える、またはランダムな敵に!crimsonEyed:M2! ダメージを5回与える。"]}
cards["crimsonEyed:Condition"] = {"NAME":"備え","DESCRIPTION":"次のターン、!B! ブロックを得る。"}
cards["crimsonEyed:Coordination"] = {"NAME":"協調","DESCRIPTION":"選択: 筋力を1得るか、集中力を1得て*朦朧を山札に加える。","UPGRADE_DESCRIPTION":"選択: 筋力を!M!得る、敏捷を!M!得る、または集中力を!M!得て*朦朧を山札に加える。"}
cards["crimsonEyed:Copycat"] = {"NAME":"模倣","DESCRIPTION":"占術!M!。 NL 山札の一番上のカードを廃棄し、そのコピーを手札に加える。","UPGRADE_DESCRIPTION":"占術!M!。 NL 山札の一番上のカードを廃棄し、そのアップグレード版のコピーを手札に加える。"}
cards["crimsonEyed:CurseMark"] = {"NAME":"呪印","DESCRIPTION":"[E][E]を得る。 NL crimsoneyed:憎悪 を crimsoneyed:激化 させる。","UPGRADE_DESCRIPTION":"[E][E][E]を得る。 NL crimsoneyed:憎悪 を crimsoneyed:激化 させる。"}
cards["crimsonEyed:CutDown"] = {"NAME":"弱点攻め","DESCRIPTION":"!D! ダメージを与える。 NL 敵が脆弱または脱力状態なら、筋力を!M!得る。"}
cards["crimsonEyed:Defend"] = {"NAME":"防御","DESCRIPTION":"!B! ブロックを得る。"}
cards["crimsonEyed:Dice"] = {"NAME":"ダイス","DESCRIPTION":"ランダムな敵に!D! ダメージを!M!回与える。"}
cards["crimsonEyed:DragonFlame"] = {"NAME":"火遁・龍炎","DESCRIPTION":"手札のスキル以外のカードを全て廃棄する。 NL !D! ダメージを与える。 NL 廃棄する。"}
cards["crimsonEyed:Endure"] = {"NAME":"耐え","DESCRIPTION":"HPを2失う。 NL !B! ブロックを得る。"}
cards["crimsonEyed:EnduringFlame"] = {"NAME":"不滅の炎","DESCRIPTION":"HPを1失う。 NL !B! ブロックを得る。 NL 何度でもアップグレードできる。"}
cards["crimsonEyed:Eye"] = {"NAME":"眼","DESCRIPTION":"集中力を!M!得る。 NL *朦朧を山札に混ぜる。"}
cards["crimsonEyed:EyesWideOpen"] = {"NAME":"眼を見開く","DESCRIPTION":"一時的な集中力を!M!得る。","UPGRADE_DESCRIPTION":"集中力を!M!得る。 NL 次の!M!ターンの終了時に集中力を1失う。"}
cards["crimsonEyed:Feet"] = {"NAME":"足技","DESCRIPTION":"敏捷を!M!得る。"}
cards["crimsonEyed:FindOpenings"] = {"NAME":"隙を突く","DESCRIPTION":"!D! ダメージを与える。 NL このターン、攻撃カードをプレイするたびにカードを1枚引く。"}
cards["crimsonEyed:Fireball"] = {"NAME":"豪火球の術","DESCRIPTION":"全ての敵に!D! ダメージを与える。廃棄済みのカード1枚につき!M! 追加ダメージ。 NL カードを1枚廃棄する。"}
cards["crimsonEyed:FromDiscardPile"] = {"NAME":"捨て札から","DESCRIPTION":"次のターン開始時、捨て札から!M!枚手札に加える。"}
cards["crimsonEyed:FromDrawPile"] = {"NAME":"山札から","DESCRIPTION":"次のターン開始時、山札から!M!枚手札に加える。"}
cards["crimsonEyed:FromExhaustPile"] = {"NAME":"廃棄札から","DESCRIPTION":"次のターン開始時、廃棄札から!M!枚手札に加える。"}
cards["crimsonEyed:Fusillade"] = {"NAME":"連射","DESCRIPTION":"!D! ダメージを与える。 NL 廃棄時: このカードのコピーを2枚手札に加える。"}
cards["crimsonEyed:Gaze"] = {"NAME":"眼差し","DESCRIPTION":"!B! ブロックを得る。 NL オーブスロットを1得る。"}
cards["crimsonEyed:Genjutsu"] = {"NAME":"幻術","DESCRIPTION":"敵の筋力を1減らす。 NL 脆弱を!crimsonEyed:M2!付与する。 NL 廃棄する。"}
cards["crimsonEyed:Grudge"] = {"NAME":"怨念","DESCRIPTION":"ターン終了時、カードを1枚廃棄する。","UPGRADE_DESCRIPTION":"初期手札。 NL ターン終了時、カードを1枚廃棄する。"}
cards["crimsonEyed:Hand"] = {"NAME":"手技","DESCRIPTION":"筋力を!M!得る。"}
cards["crimsonEyed:Hatred"] = {"NAME":"憎悪","DESCRIPTION":"プレイ不可。 NL エーテル。 NL ターン終了時、HPを!M!失う。デッキから取り除けない。"}
cards["crimsonEyed:Honoikazuchi"] = {"NAME":"焔雷","DESCRIPTION":"このバトルで生成したダーク1つにつき!D! ダメージを与える。","EXTENDED_DESCRIPTION":[" NL （ダークを!M!個生成済み。）"]}
cards["crimsonEyed:HungerForPower"] = {"NAME":"力への渇望","DESCRIPTION":"カードを!M!枚引く。 NL この方法で引いた状態異常またはカースカードを廃棄し、廃棄した枚数だけ追加で引く。"}
cards["crimsonEyed:IndraForm"] = {"NAME":"インドラの型","DESCRIPTION":"エーテル。 NL ターン開始時、ライトニングを!M!個生成する。","UPGRADE_DESCRIPTION":"ターン開始時、ライトニングを!M!個生成する。"}
cards["crimsonEyed:IndrasArrow"] = {"NAME":"インドラの矢","DESCRIPTION":"このバトルで生成したライトニング1つにつきコストが[E]1減る。 NL !D! ダメージを与える。"}
cards["crimsonEyed:InfernoStyle"] = {"NAME":"炎遁の型","DESCRIPTION":"ダーク1つを生成する。 NL ダークオーブがパッシブ効果を発動するたびに、crimsoneyed:炎バリア を!M!得る。"}
cards["crimsonEyed:Izanagi"] = {"NAME":"伊邪那岐","DESCRIPTION":"無実体を!M!得る。 NL ターン終了時、*虚無を山札に混ぜる。"}
cards["crimsonEyed:Jolt"] = {"NAME":"放電","DESCRIPTION":"!D! ダメージを与える。 NL 次のオーブを解放する。 NL カードを1枚引く。"}
cards["crimsonEyed:Kagutsuchi"] = {"NAME":"加具土命","DESCRIPTION":"HPを1失う。 NL ロックオンを1付与する。 NL 次のオーブを解放する。","UPGRADE_DESCRIPTION":"HPを1失う。 NL ロックオンを1付与する。 NL 次のオーブを2回解放する。"}
cards["crimsonEyed:KagutsuchiChidori"] = {"NAME":"加具土命千鳥","DESCRIPTION":"!D! ダメージを与える。 NL 選択: ライトニングまたはダークを1個生成する。 NL 廃棄する。","UPGRADE_DESCRIPTION":"!D! ダメージを与える。 NL 選択: ライトニングまたはダークを1個生成する。","EXTENDED_DESCRIPTION":["!D! ダメージを与える。 NL 選択: ライトニング、ダーク、またはプラズマを1個生成する。 NL 廃棄する。","!D! ダメージを与える。 NL 選択: ライトニング、ダーク、またはプラズマを1個生成する。"]}
cards["crimsonEyed:KillingIntent"] = {"NAME":"殺意","DESCRIPTION":"!D! ダメージを与える。 NL 脱力を!M!付与する。 NL 脆弱を!M!付与する。 NL crimsoneyed:憎悪 を crimsoneyed:激化 させる。","UPGRADE_DESCRIPTION":"!D! ダメージを与える。 NL 脱力を!M!付与する。 NL 脆弱を!M!付与する。"}
cards["crimsonEyed:Kirin3"] = {"NAME":"麒麟","DESCRIPTION":"廃棄済みのカード1枚につきコストが[E]1減る。 NL ライトニングを!M!個生成する。 NL 全てのオーブを解放する。 NL 廃棄する。"}
cards["crimsonEyed:KnowPain"] = {"NAME":"痛みを知れ","DESCRIPTION":"ターン開始時、crimsoneyed:憎悪 を crimsoneyed:激化 させ、カードを!M!枚引く。","UPGRADE_DESCRIPTION":"初期手札。 NL ターン開始時、crimsoneyed:憎悪 を crimsoneyed:激化 させ、カードを!M!枚引く。"}

cards["crimsonEyed:LightningSpeed"] = {"NAME":"雷速","DESCRIPTION":"ライトニングを NL 生成するたびに、ブロックを!M!得る。 NL ライトニング1つを生成する。","UPGRADE_DESCRIPTION":"初期手札。 NL ライトニングを NL 生成するたびに、ブロックを!M!得る。 NL ライトニング1つを生成する。"}
cards["crimsonEyed:LionsBarrage"] = {"NAME":"獅子連弾","DESCRIPTION":"!D! ダメージを!M!回与える。"}
cards["crimsonEyed:Mangekyou"] = {"NAME":"万華鏡写輪眼","DESCRIPTION":"ターン終了時、HPを!M!失い、集中力を!M!得る。"}
cards["crimsonEyed:Mangekyou2"] = {"NAME":"万華鏡写輪眼","DESCRIPTION":"カードによってHPを失うたびに、 NL 集中力を!M!得る。"}
cards["crimsonEyed:MindControl"] = {"NAME":"支配","DESCRIPTION":"初期手札。 NL 敵が攻撃意図を持つなら脱力を!M!付与する。 NL そうでなければ脆弱を!M!付与する。 NL 廃棄する。"}
cards["crimsonEyed:MindGames"] = {"NAME":"心理戦","DESCRIPTION":"!B! ブロックを得る。 NL このターンに占術を行った場合、筋力を!M!得る。"}
cards["crimsonEyed:OneStepAhead"] = {"NAME":"先読み","DESCRIPTION":"カードを!M!枚引く。 NL 占術1。"}
cards["crimsonEyed:PaperBomb"] = {"NAME":"起爆札","DESCRIPTION":"シヴを!crimsonEyed:M2!枚手札に加える。廃棄時: NL 全ての敵に!M! ダメージを与える。","UPGRADE_DESCRIPTION":"シヴを!crimsonEyed:M2!枚手札に加える。廃棄時: NL 全ての敵に!M! ダメージを与える。"}
cards["crimsonEyed:Parry"] = {"NAME":"受け流し","DESCRIPTION":"!B! ブロックを得る。 NL 脱力を!M!付与する。"}
cards["crimsonEyed:Payback"] = {"NAME":"報復","DESCRIPTION":"!D! ダメージを与える。 NL 敵が脱力または脆弱状態なら、 NL [E][E]を得る。","UPGRADE_DESCRIPTION":"!D! ダメージを与える。 NL 敵が脱力または脆弱状態なら、 NL [E][E][E]を得る。"}
cards["crimsonEyed:Perception"] = {"NAME":"知覚","DESCRIPTION":"占術を行うたびに、カードを!M!枚引く。","UPGRADE_DESCRIPTION":"初期手札。 NL 占術を行うたびに、カードを!M!枚引く。"}
cards["crimsonEyed:PeripheralVision"] = {"NAME":"広域視野","DESCRIPTION":"バトル中の敵1体につき!B! ブロックを得る。"}
cards["crimsonEyed:PhoenixFlower2"] = {"NAME":"不死鳥花","DESCRIPTION":"カードを廃棄するたびに、ランダムな敵に!M! ダメージを与える。"}
cards["crimsonEyed:PlanetaryDevastation"] = {"NAME":"惑星壊滅","DESCRIPTION":"ロックオンを!M!付与する。 NL オーブスロットを!crimsonEyed:M2!得る。プラズマを!crimsonEyed:M2!個生成する。 NL 廃棄する。"}
cards["crimsonEyed:PullWires"] = {"NAME":"策謀","DESCRIPTION":"シヴを!M!枚手札に加える。 NL 捨て札のカードを1枚山札の一番上に置く。","UPGRADE_DESCRIPTION":"アップグレード済みシヴを!M!枚手札に加える。 NL 捨て札のカードを1枚山札の一番上に置く。"}
cards["crimsonEyed:React"] = {"NAME":"反応","DESCRIPTION":"次のターン、追加でカードを!M!枚引く。","UPGRADE_DESCRIPTION":"次のターン、追加でカードを!M!枚引く。"}
cards["crimsonEyed:Read"] = {"NAME":"構え","DESCRIPTION":"次のターン、[E]を得る。","UPGRADE_DESCRIPTION":"次のターン、[E][E]を得る。"}
cards["crimsonEyed:Rend"] = {"NAME":"斬撃","DESCRIPTION":"全ての敵に!D! ダメージを与える。"}
cards["crimsonEyed:Resentment"] = {"NAME":"怨恨","DESCRIPTION":"エーテル。 NL カードを!M!枚廃棄する。 NL 廃棄する。","UPGRADE_DESCRIPTION":"エーテル。 NL カードを!M!枚廃棄する。 NL 廃棄する。"}
cards["crimsonEyed:Revenge"] = {"NAME":"復讐","DESCRIPTION":"!D! ダメージを!M!回与える。 NL このバトルでHPを失った回数だけ追加でヒットする。 NL 廃棄する。"}
cards["crimsonEyed:Revolution"] = {"NAME":"革命","DESCRIPTION":"状態異常またはカースカードを引くたびに、筋力を!M!得る。","UPGRADE_DESCRIPTION":"初期手札。 NL 状態異常またはカースカードを引くたびに、筋力を!M!得る。"}
cards["crimsonEyed:SeeEverything"] = {"NAME":"全てを見通す","DESCRIPTION":"全ての敵にロックオン、脆弱、脱力をX付与する。 NL 廃棄する。","UPGRADE_DESCRIPTION":"全ての敵にロックオン、脆弱、脱力をX+1付与する。 NL 廃棄する。"}
cards["crimsonEyed:SeverThePast"] = {"NAME":"過去を断ち切る","DESCRIPTION":"廃棄済みのカード1枚につき!M! ブロックを得る。 NL 捨て札からカードを1枚廃棄する。","EXTENDED_DESCRIPTION":[" NL （ブロック!B!を得る。）"]}
cards["crimsonEyed:ShadowShuriken"] = {"NAME":"影手裏剣","DESCRIPTION":"!D! ダメージを与える。 NL シヴを!M!枚手札に加える。"}
cards["crimsonEyed:Sharingan"] = {"NAME":"写輪眼","DESCRIPTION":"ロックオンを2付与する。 NL 占術!M!。","UPGRADE_DESCRIPTION":"ロックオンを2付与する。 NL 占術!M!。 NL カードを1枚引く。 NL crimsoneyed:憎悪 を crimsoneyed:激化 させる。"}
cards["crimsonEyed:ShedSkin"] = {"NAME":"脱皮","DESCRIPTION":"カードを1枚廃棄する。 NL 状態異常またはカースカードだった場合、*リジェネ を!M!得て廃棄する。"}
cards["crimsonEyed:Shurikenjutsu"] = {"NAME":"手裏剣術","DESCRIPTION":"手札を NL シヴで満たす。 NL 廃棄する。","UPGRADE_DESCRIPTION":"手札を NL シヴで満たす。"}
cards["crimsonEyed:SixthSense"] = {"NAME":"第六感","DESCRIPTION":"!B! ブロックを得る。占術を行うたびに、捨て札にあるこのカードを手札に戻す。"}
cards["crimsonEyed:SkeletonShield"] = {"NAME":"骨の盾","DESCRIPTION":"!B! ブロックを得る。 NL 金属化を!M!得る。"}
cards["crimsonEyed:Slash"] = {"NAME":"斬","DESCRIPTION":"!D! ダメージを与える。"}
cards["crimsonEyed:Slither"] = {"NAME":"這う","DESCRIPTION":"カードを!M!枚引く。 NL *粘液を山札の一番上に置く。"}
cards["crimsonEyed:SnakeBinding"] = {"NAME":"蛇縛り","DESCRIPTION":"このターン、全ての敵の筋力を!M!減らす。 NL *粘液を手札に加える。"}
cards["crimsonEyed:SnakeBite"] = {"NAME":"蛇咬み","DESCRIPTION":"!D! ダメージを与える。 NL ブロックを無視したダメージと等しい毒を付与する。"}
cards["crimsonEyed:SnakeHands"] = {"NAME":"蛇の手","DESCRIPTION":"!D! ダメージを与える。 NL 手札に状態異常またはカースカードがある場合、3回ヒットする。"}
cards["crimsonEyed:SpaceTime"] = {"NAME":"時空間術","DESCRIPTION":"選択: NL *万象引力 または *天手力 を手札に加える。","UPGRADE_DESCRIPTION":"選択: NL *万象引力+ または *天手力+ を手札に加える。","EXTENDED_DESCRIPTION":["選択: NL *万象引力、*天手力、または *万象斥力 を手札に加える。","選択: NL *万象引力+、*天手力+、または *万象斥力+ を手札に加える。"]}
cards["crimsonEyed:Spite2"] = {"NAME":"悪意","DESCRIPTION":"エーテル。 NL !D! ダメージを与える。ブロックを無視したダメージと等しいHPを回復する。 NL 廃棄する。","UPGRADE_DESCRIPTION":"!D! ダメージを与える。ブロックを無視したダメージと等しいHPを回復する。 NL 廃棄する。"}
cards["crimsonEyed:Strike"] = {"NAME":"打撃","DESCRIPTION":"!D! ダメージを与える。"}
cards["crimsonEyed:SummonGaruda"] = {"NAME":"口寄せ・迦楼羅","DESCRIPTION":"!D! ダメージを与える。 NL カードを!M!枚引く。 NL 廃棄する。"}
cards["crimsonEyed:SummonWeapons"] = {"NAME":"口寄せ・武器","DESCRIPTION":"初期手札。 NL シヴを!M!枚手札に加える。 NL 廃棄する。","UPGRADE_DESCRIPTION":"初期手札。 NL シヴを!M!枚手札に加える。"}
cards["crimsonEyed:Susanoo"] = {"NAME":"須佐能乎","DESCRIPTION":"このバトルでHPを失った回数につきコストが[E]1減る。 NL *金属化 を!M!得る。"}
cards["crimsonEyed:Tomoe"] = {"NAME":"巴","DESCRIPTION":"占術!M!。 NL 空のオーブスロットがない場合、集中力を1得る。"}
cards["crimsonEyed:Tsukuyomi"] = {"NAME":"月読","DESCRIPTION":"HPを1失う。 NL 脆弱を!crimsonEyed:M2!付与する。 NL 敵のデバフ1つにつき敵のHPを!M!減らす。"}
cards["crimsonEyed:UniversalPull"] = {"NAME":"万象引力","DESCRIPTION":"どこからでも!M!枚のカードを NL 次のターンに手札に加える。","UPGRADE_DESCRIPTION":"どこからでも!M!枚のカードを NL 次のターンに手札に加える。"}
cards["crimsonEyed:Vantage"] = {"NAME":"優位","DESCRIPTION":"初期手札。 NL [E]を得る。 NL 廃棄する。","UPGRADE_DESCRIPTION":"初期手札。 NL [E]を得る。"}
cards["crimsonEyed:ViciousStrike"] = {"NAME":"凶撃","DESCRIPTION":"!D! ダメージを与える。 NL カードを1枚引く。 NL crimsoneyed:憎悪 を crimsoneyed:激化 させる。"}
cards["crimsonEyed:WatchOut"] = {"NAME":"警戒","DESCRIPTION":"!B! ブロックを得る。 NL 全ての敵にロックオンを!M!付与する。"}
cards["crimsonEyed:YasakaMagatama2"] = {"NAME":"八坂の勾玉","DESCRIPTION":"ランダムな敵に!D! ダメージを与えつつ脱力を1付与することを3回繰り返す。 NL *燃焼を捨て札に加える。"}
cards["crimsonEyed:LightningChoice"] = {"NAME":"ライトニング","DESCRIPTION":"ライトニング1つを生成する。"}
cards["crimsonEyed:DarkChoice"] = {"NAME":"ダーク","DESCRIPTION":"ダーク1つを生成する。"}
cards["crimsonEyed:PlasmaChoice"] = {"NAME":"プラズマ","DESCRIPTION":"プラズマ1つを生成する。"}

with open(f"{out}/SasukeMod-Card-Strings.json","w",encoding="utf-8") as f:
    json.dump(cards,f,ensure_ascii=False,indent=2)
print("Cards: OK")

character = {"crimsonEyed:Sasuke":{"NAMES":["うちはサスケ","うちはサスケ"],"TEXT":["復讐に生きる うちはサスケ。 NL 雷遁と写輪眼で敵を圧倒する。","NL 千鳥に黒炎を纏わせる...","暗い路地を進むと、何者かが不気味な儀式を行っているのに出くわした。近づくと、一斉にこちらを振り向く。最も背の高い者が鋭い牙を剥き出しにし、白く長い手を伸ばしてきた。 NL ~「共に~来い~兄よ、~スパイアの~温もりを~感じるがいい。」~"]}}
with open(f"{out}/SasukeMod-Character-Strings.json","w",encoding="utf-8") as f:
    json.dump(character,f,ensure_ascii=False,indent=2)
print("Character: OK")

keywords = [{"PROPER_NAME":"起爆","NAMES":["explosive","Explosive","起爆"],"DESCRIPTION":"次にカードを廃棄した時、敵にダメージを与える。"},{"PROPER_NAME":"憎悪","NAMES":["hatred","Hatred","Hatreds","憎悪"],"DESCRIPTION":"憎悪はエーテル付きのカースで、毎ターンHPを失わせる。"},{"PROPER_NAME":"運命","NAMES":["fate","Fate","運命"],"DESCRIPTION":"次のバフを無効化する。アーティファクトを通じて付与される。"},{"PROPER_NAME":"炎バリア","NAMES":["Flame Barrier","flame_barrier","Flame_Barrier","炎バリア"],"DESCRIPTION":"このターン攻撃を受けるたびに、ダメージを反射する。"},{"PROPER_NAME":"激化","NAMES":["intensify","Intensify","激化"],"DESCRIPTION":"手札にある憎悪をアップグレードし、その他の憎悪を全て手札に加える。持っていない場合はコピーを1枚手札に加える。"},{"PROPER_NAME":"占術済み","NAMES":["Scried","占術済み"],"DESCRIPTION":"山札の上X枚を見る。任意の枚数を捨て札にできる。"}]
with open(f"{out}/SasukeMod-Keyword-Strings.json","w",encoding="utf-8") as f:
    json.dump(keywords,f,ensure_ascii=False,indent=2)
print("Keywords: OK")

potions = {"crimsonEyed:CoordinationPotion":{"NAME":"協調のポーション","DESCRIPTIONS":["#y筋力 、#y敏捷 、#y集中力 をそれぞれ #b"," 得る。"]},"crimsonEyed:ParalysisPotion":{"NAME":"麻痺のポーション","DESCRIPTIONS":["敵の #y筋力 を #b"," 減らす。"]},"crimsonEyed:ScryPotion":{"NAME":"占術のポーション","DESCRIPTIONS":["占術を #b"," 行う。次のターン、追加でカードを1枚引く。"]},"crimsonEyed:YinVessel":{"NAME":"陰の器","DESCRIPTIONS":["ランダムなレアカード #b5 枚（他の各キャラクター1枚ずつ）から #b1 枚を選んで手札に加える。このターン、そのカードのコストは #b0 になる。","ランダムなレアカード #b5 枚（他の各キャラクター1枚ずつ）から1枚を選び、 #b2 枚のコピーを手札に加える。このターン、それらのコストは #b0 になる。"]}}
with open(f"{out}/SasukeMod-Potion-Strings.json","w",encoding="utf-8") as f:
    json.dump(potions,f,ensure_ascii=False,indent=2)
print("Potions: OK")

powers = {"crimsonEyed:BlazeBarrierPower":{"NAME":"炎壁","DESCRIPTIONS":["#yダーク オーブがパッシブ効果を発動するたびに、#y炎バリア を #b"," 得る。"]},"crimsonEyed:BlindedPower":{"NAME":"盲目","DESCRIPTIONS":["ターン終了時、#y虚無 を #b"," 枚山札に混ぜる。","ターン終了時、#y虚無 を1枚山札に混ぜる。"]},"crimsonEyed:ElectrifyPower":{"NAME":"帯電","DESCRIPTIONS":["次の #b"," ターン、#yライトニング が全ての敵にヒットする。","このターン、#yライトニング が全ての敵にヒットする。"]},"crimsonEyed:ExhaustDamagePower":{"NAME":"不死鳥花","DESCRIPTIONS":["カードを廃棄するたびに、ランダムな敵に #b"," ダメージを与える。"]},"crimsonEyed:FindOpeningsPower":{"NAME":"隙を突く","DESCRIPTIONS":["攻撃カードをプレイするたびに、カードを #b"," 枚引く。"," 枚引く。"]},"crimsonEyed:GrudgePower":{"NAME":"怨念","DESCRIPTIONS":["ターン終了時、カードを #b"," 枚廃棄する。"," 枚廃棄する。"]},"crimsonEyed:IndraFormPower":{"NAME":"インドラの型","DESCRIPTIONS":["ターン開始時、#yライトニング を #b"," 個生成する。"]},"crimsonEyed:KagutsuchiPower":{"NAME":"加具土命","DESCRIPTIONS":["このターン、攻撃カードをプレイするたびに次のオーブのパッシブ効果を #b"," 回発動する。"," 回発動する。"]},"crimsonEyed:LightningSpeedPower":{"NAME":"雷速","DESCRIPTIONS":["#yライトニング を生成するたびに、#yブロック を #b"," 得る。"]},"crimsonEyed:LoseFocusPower":{"NAME":"集中力消散","DESCRIPTIONS":["ターン終了時、#y集中力 を #b"," 失う。"]},"crimsonEyed:MangekyouPower2":{"NAME":"万華鏡写輪眼","DESCRIPTIONS":["カードによってHPを失うたびに、#y集中力 を #b"," 得る。"]},"crimsonEyed:OneStepAheadPower":{"NAME":"先読み","DESCRIPTIONS":["このターン終了時、最大 #b"," 枚のカードを保留する。"," 枚のカードを保留する。"]},"crimsonEyed:PerceptionPower":{"NAME":"知覚","DESCRIPTIONS":["占術を行うたびに、カードを #b"," 枚引く。"," 枚引く。"]},"crimsonEyed:KnowPainPower":{"NAME":"痛みを知れ","DESCRIPTIONS":["ターン開始時、#y憎悪 を #y激化 させ、カードを #b"," 枚引く。"," 枚引く。"]},"crimsonEyed:RevolutionPower":{"NAME":"革命","DESCRIPTIONS":["状態異常またはカースカードを引くたびに、#y筋力 を #b"," 得る。"]},"crimsonEyed:SpitePower":{"NAME":"悪意","DESCRIPTIONS":["致死ダメージを与えるたびに、HP を #b"," 回復する。"]},"crimsonEyed:SpaceTimePower":{"NAME":"万象引力","DESCRIPTIONS":["あと #b"," ターン後、"," を手札に加える。"," ターン後、"]}}
with open(f"{out}/SasukeMod-Power-Strings.json","w",encoding="utf-8") as f:
    json.dump(powers,f,ensure_ascii=False,indent=2)
print("Powers: OK")

relics = {"crimsonEyed:CrimsonEye":{"NAME":"DEPRECATED:紅眼（旧版）","FLAVOR":"一つの眼。その虹彩がかすかに赤く脈動している。","DESCRIPTIONS":["各バトル開始時、全ての敵にロックオンを #b1 付与する。"]},"crimsonEyed:CrimsonEye2":{"NAME":"紅眼","FLAVOR":"#y憎悪 に染まりし眼。真実を見通し、幻を創り出す。","DESCRIPTIONS":["HPが #b50% 以下の時、#y筋力 、#y敏捷 、#y集中力 が #b"," ずつ増加する。"]},"crimsonEyed:CrowFeather":{"NAME":"烏の羽","FLAVOR":"手のひらにその感触はある。しかし本当にそこにあるのか、確信が持てない。","DESCRIPTIONS":["敵にデバフを付与するたびに、#yブロック を #b"," 得る。"]},"crimsonEyed:EternalEye":{"NAME":"永遠の眼","FLAVOR":"闇の中から目覚めし眼。","DESCRIPTIONS":["#y紅眼 を置き換える。バトル開始時、#y筋力 、#y敏捷 、#y集中力 が #b"," ずつ増加した状態で始まる。"]},"crimsonEyed:BlueScale":{"NAME":"青い鱗","FLAVOR":"青い蛇の鱗。長い間閉ざしていた何かを揺り起こす。","DESCRIPTIONS":["各ターン、初めて状態異常またはカースカードを引いた時、[E]を得る。"]},"crimsonEyed:CherryBlossom":{"NAME":"桜","FLAVOR":"咲き誇る生命力。","DESCRIPTIONS":["バトル中、初めてカードを #b"," 枚廃棄した時、HP を #b"," 回復する。"]},"crimsonEyed:NohMask":{"NAME":"能面","FLAVOR":"死神の面。これを被る者は、生と死の十字路に立つ。","DESCRIPTIONS":["「選択」カードの選択肢が少なくとも #b3 つになる。"]},"crimsonEyed:PaperSnek":{"NAME":"紙の蛇","FLAVOR":"折り目の曲線が、うねる生き物の姿を描き出している。","DESCRIPTIONS":["#yロックオン 状態の敵が受けるダメージが #b50% 増ではなく #b75% 増になる。"]},"crimsonEyed:Kaleidoscope":{"NAME":"万華鏡","FLAVOR":"無数の色彩。","DESCRIPTIONS":["各バトル開始時、全ての敵に #yロックオン を #b"," 付与する。"]},"crimsonEyed:ScratchedHeadband":{"NAME":"傷ついた額当て","FLAVOR":"かつて歪み、曲がりながらも、決して断ち切られなかった絆の形見。まるで祈るように、強く握り締める。","DESCRIPTIONS":["#y憎悪 を #y不滅の炎+ に変換する。#y激化 は代わりに #y不滅の炎 に作用する。"]},"crimsonEyed:StoneTablet":{"NAME":"石板","FLAVOR":"見たこともない言語で刻まれた予言。それでもなぜか、その言葉が理解できる...","DESCRIPTIONS":["前のターンにHPを失っていた場合、ターン開始時に占術を #b"," 行う。"]},"crimsonEyed:StoneTabletOLD":{"NAME":"DEPRECATED:石板（旧版）","FLAVOR":"見たこともない言語で刻まれた予言。なぜか読める。","DESCRIPTIONS":["占術を #b"," 回行うたびに、全ての敵に #b"," ダメージを与える。"]},"crimsonEyed:Uchiwa":{"NAME":"団扇","FLAVOR":"紙の扇子。かつて戦場で兵を導くために用いられたものかもしれない。","DESCRIPTIONS":["#y初期手札 のカードを引くたびに、カードを #b1 枚引く。"]}}
with open(f"{out}/SasukeMod-Relic-Strings.json","w",encoding="utf-8") as f:
    json.dump(relics,f,ensure_ascii=False,indent=2)
print("Relics: OK")

print("\n=== 全ファイル生成完了 ===")
import os
for fn in sorted(os.listdir(out)):
    print(f"  {fn}")
