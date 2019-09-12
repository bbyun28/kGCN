import os

#-------------------------------------------------------------------------------
# コマンドライン引数が正しく指定されて稲生場合は、使用方法を表示して異常終了
#-------------------------------------------------------------------------------
def if_usage_is_correct(min_args_num, argv, args_str):
    """
    コマンドライン引数が正しく指定されて稲生場合は、使用方法を表示して異常終了
    【引数】
    min_args_num: 最低限必要なコマンドライン引数の数
    argv: コマンドライン入力が格納されたリスト
    args_str: 使用方法を表示するためのコマンドライン引数文字列
    """
    if len(argv) < min_args_num + 1:
        print(" (Usage) python {} {}".format(argv[0], args_str))
        exit(1)


#-------------------------------------------------------------------------------
# 指定したディレクトリが存在しない場合は、エラーメッセージを表示して異常終了
#-------------------------------------------------------------------------------
def if_directory_is_exist(dirname):
    """
    指定したファイルが存在するかどうかチェックする。
    ファイルが存在しない場合は、エラーメッセージを表示して異常終了する
    【引数】
    filename: ファイル名
    """
    if not os.path.isdir(dirname):
        print("### (Error) ディレクトリ\"{}\"が存在しません。 ###".format(dirname))
        exit(1)

#-------------------------------------------------------------------------------
# 指定したファイルが存在するかどうかチェックする。
#-------------------------------------------------------------------------------
def if_file_is_exist(filename):
    """
    指定したファイルが存在するかどうかチェックする。
    ファイルが存在しない場合は、エラーメッセージを表示して異常終了する
    【引数】
    filename: ファイル名
    """
    if not os.path.isfile(filename):
        print("### (Error) ファイル\"{}\"が存在しません。 ###".format(filename))
        exit(1)