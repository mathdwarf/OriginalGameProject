# Original Game Project

## ■game_01

## ◆確認環境

    Python >= 3.9

## ◆最初にすること

いつものやつ。

    cd game_01
    pip install -r requirements.txt

## ◆キャラクターデータの確認方法

### ●元となっているcsvデータファイルの場所

    game_01/static/csv/
        characters.csv  : 全キャラクターのステータス一覧
        actions.csv     : 戦闘時にとれる行動の一覧

csvファイルはGoogle Spreadsheetで編集→エクスポートしている。そのほうが効率的だし。

### ●全キャラクターのステータス確認方法

    cd game_01
    python

    >>> from characters import Characters
    >>> characters = Characters()
    >>> characters.show_all()

注意：csvにいるキャラクターデータが全部出る。  
　　　各キャラクターが戦闘時にとれる行動も出力されるのでキャラクター多いとやばい。  
　　　キャラクター増やした後は何らかのファイルに出力することをおすすめする。

#### ●キャラクターの召喚方法（ランダム編）

キャラクターの召喚方法は以下。引数なしだとひとり召喚される。  
引数に数値入れるとその数値の人数召喚する。  
なお召喚されるキャラクターのキャラかぶりは考慮してない。  
テスト中4人同じやつとかあった。

    >>> characters.summon_random()
    >>> characters.summon_random(3)

誰が召喚されているかを確認する方法は以下。

    >>> characters.show_summoned()

おわかりかもしれないけれど、めっちゃ召喚してるとめっちゃ出力される。注意。

以上。  
