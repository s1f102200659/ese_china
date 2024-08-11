from django.shortcuts import render
from .forms import TranslationForm
from django.http import HttpResponse
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def index(request):
    return render(request, 'index.html')

def translate_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        OPENAI_API_KEY = '自身のAPIキー'
        OPENAI_API_BASE = "エンドポイントを設定"

        chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, openai_api_base=OPENAI_API_BASE, model_name='gpt-4o', temperature=0)
        kyouyuu = [
            HumanMessage(content=f"""これから打つ文章をすべて日本語の漢字から構成される単語のみに変換してください。
                          偽物の中国語っぽい文章にしてください。漢字のみにしてください。 絶対に守る条件： 中国語の単語は使いません
                          文章を変換した後の文章は日本語の漢字のみになるようにします。 カタカナやひらがなは絶対に何があっても使ってはいけません。
                          今日の天気は良いなどの場合の接続語の、の、は、がも使ってはいけません。 
                          主語が存在しない場合で相手のことについて質問している場合には其方を主語としてください。 例:私→我、あなた→其方、ありがとう→感謝 今日→本日 良いなどの動詞も単語の良好に変換。 
                          例文：私は学校に行きます→我学校行成 絶対にひらがなやカタカナが文章の中に入らないようにしてください。
                          カタカナの単語はうまく漢字だけで変換してください 例:ハンバーグ→挽肉捏焼物  
                          人命が入力された場合には当て字で対応してください 例:ヘルナンデス→屁瑠難出巣
                          こんばんは→例:夜挨拶
                        """ + "\n" + input_text)
        ]
        print(chat(kyouyuu).content)
        translated_text = f"翻訳結果: {chat(kyouyuu).content}"  # 簡単な例
        return render(request,'index.html',{'translated_text':translated_text})  # 結果をHTTPレスポンスとして返す
    return render(request, 'your_template.html')  # GETリクエストの場合