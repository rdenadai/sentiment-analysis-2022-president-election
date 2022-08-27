# Sentiment Analysis for 2018 Presidential Election

Análise de sentimentos relacionados aos candidatos a Eleição para a presidência de 2022.

### Motivação

Este repositório é um follow-up da análise realizada em 2018 para uma disciplina de mestrado na Unicamp.

A época foram avaliadas as redes sociais e o possível impacto que elas poderiam ter sobre as eleições presidenciais, avaliando a dimensão dos sentimentos que prevaleciam nas redes a época.

Para rever o levantamente realizado em 2018 acesse o antigo repositório [Sentiment Analysis for 2018 Presidential Election](https://github.com/rdenadai/sentiment-analysis-2018-president-election).

### Objetivo

Analisar as valências e emoções em comentários (textos) das principais redes sociais utilizadas no Brasil: Instagram, Facebook, Twitter (Tweets e Tendências) e Youtube referentes a eleição para presidente do Brasil em 2018.

### Abordagem Proposta

Utilizar modelo de emoção categórico baseado em emoções com uma abordagem supervisionada composta por três etapas:

 - *Coleta dos comentários* - coletar comentários dos candidatos melhores classificados nas pesquisas eleitorais para presidente (Jair Bolsonaro, Lula, e Ciro Gomes) nas redes sociais (Facebook, Instagram, Twitter e Youtube);

 - *Classificação dos comentários* - tratar os comentários e realizar testes para escolher o melhor classificador e os melhores datasets a serem utilizados para gerar categorizar as emoções nos comentários coletados;

 - *Análise dos resultados* - analisar os resultados obtidos, após a classificação dos comentários para tentar entender o papel das emoções no resultado da eleição para presidente no Brasil e apresentar um panorama de influência entre o eleitorado.

### Origem dos dados

#### Twitter Hashtags:

##### **Bolsonaro**
---
[#Bolsonaro22](https://twitter.com/search?q=%23Bolsonaro22&src=typed_query&f=live),
[#BrasilComBolsonaro](https://twitter.com/search?q=%23BrasilComBolsonaro&src=typed_query&f=live),
[#BrasilComBolsonaro22](https://twitter.com/search?q=%23BrasilComBolsonaro22&src=typed_query&f=live),
[#BolsonaroReeleitoEm2022](https://twitter.com/search?q=%23BolsonaroReeleitoEm2022&src=typed_query&f=live),
[#BolsonaroNoPrimeiroTurno](https://twitter.com/search?q=%23BolsonaroNoPrimeiroTurno&src=typed_query&f=live),
[#CapitaoDoPovoVaiVencerDeNovo](https://twitter.com/search?q=%23CapitaoDoPovoVaiVencerDeNovo&src=typed_query&f=live),
[#BolsonaroNoPanico](https://twitter.com/search?q=%23BolsonaroNoPanico&src=typed_query&f=live),
[#BolsonaroNoFlow](https://twitter.com/search?q=%23BolsonaroNoFlow&src=typed_query&f=live),
[#BolsonaroNoJN](https://twitter.com/search?q=%23BolsonaroNoJN&src=typed_query&f=live),
[#EJairOuJaEra](https://twitter.com/search?q=%23EJairOuJaEra&src=typed_query&f=live),
[#BolsonaroNoIronberg](https://twitter.com/search?q=%23BolsonaroNoIronberg&src=typed_query&f=live),
[#CapitaoDoPovoVaiVencerDeNovo](https://twitter.com/search?q=%23CapitaoDoPovoVaiVencerDeNovo&src=typed_query&f=live)
[#BolsonaroMentiroso](https://twitter.com/search?q=%23BolsonaroMentiroso&src=typed_query&f=live),
[#MentirosoNoJN](https://twitter.com/search?q=%23MentirosoNoJN&src=typed_query&f=live),
[#ForaBolsonaroMentiroso](https://twitter.com/search?q=%23ForaBolsonaroMentiroso&src=typed_query&f=live),
["BOLSONARO CAGÃO"](https://twitter.com/search?q=%22BOLSONARO%20CAG%C3%83O%22&&src=typed_query&f=livey),
[#BolsonaroGenocida](https://twitter.com/search?q=%23BolsonaroGenocida&src=typed_query&f=live),

##### **Lula**
---
[#LulaPresidente13](https://twitter.com/search?q=%23LulaPresidente13&src=typed_query&f=live),
[#LulaPresidente](https://twitter.com/search?q=%23LulaPresidente&src=typed_query&f=live),
[#Lula2022](https://twitter.com/search?q=%23Lula2022&src=typed_query&f=live),
[#BrasilDaEsperança](https://twitter.com/search?q=%23BrasilDaEsperan%C3%A7a&src=typed_query&f=live),
[#Vote13](https://twitter.com/search?q=%23Vote13&src=typed_query&f=live),
[#LulaNoJN](https://twitter.com/search?q=%23LulaNoJN&src=typed_query&f=live),
["Lulinha"](https://twitter.com/search?q=%22Lulinha%22&src=typed_query&f=live),
[#LulaLadraoSeuLugarENaPrisao](https://twitter.com/search?q=%23LulaLadraoSeuLugarENaPrisao&src=typed_query&f=live),
[#LADRAONOJN](https://twitter.com/search?q=%23LADRAONOJN&src=typed_query&f=live),
[#BonnerTchutchucaDoLadrao](https://twitter.com/search?q=%23BonnerTchutchucaDoLadrao&src=typed_query&f=live),
[#PTNuncaMais](https://twitter.com/search?q=%23PTNuncaMais&src=typed_query&f=live),
[#DerreteLula](https://twitter.com/search?q=%23DerreteLula&src=typed_query&f=live)

##### **Ciro**
---
[#CiroPresidente12](https://twitter.com/search?q=%23CiroPresidente12&src=typed_query&f=live),
[#Ciro2022](https://twitter.com/search?q=%23Ciro2022&src=typed_query&f=live),
[#CiroGomes](https://twitter.com/search?q=%23CiroGomes&src=typed_query&f=live),
[#PrefiroCiro](https://twitter.com/search?q=%23PrefiroCiro&src=typed_query&f=live)
[#CiristaSegueCirista](https://twitter.com/search?q=%23CiristaSegueCirista&src=typed_query&f=live),
[#CiroNoJN](https://twitter.com/search?q=%23CiroNoJN&src=typed_query&f=live),
[#cironojornalnacional](https://twitter.com/search?q=%23cironojornalnacional&src=typed_query&f=live)

##### **Simone Tebet**
---
[#SimoneTebet](https://twitter.com/hashtag/SimoneTebet?src=hashtag_click&f=live),
[#SimonePresidente15](https://twitter.com/hashtag/SimonePresidente15?src=hashtag_click&f=live),
[#SimonenoJN](https://twitter.com/search?q=%23SimonenoJN&src=typed_query&f=live),
[#SimoneTebetNoJN](https://twitter.com/hashtag/SimoneTebetNoJN?src=hashtag_click&f=live)

##### **Geral**
---
["Meu Presidente"](https://twitter.com/search?q=%22Meu%20Presidente%22&src=typed_query&f=live),
[#É22](https://twitter.com/search?q=%23%C3%8922&src=typed_query&f=live),
[#É13](https://twitter.com/search?q=%23%C3%8913&src=typed_query&f=live),
[#É12](https://twitter.com/search?q=%23%C3%8912&src=typed_query&f=live),
[#Eleicoes2022](https://twitter.com/search?q=%23Eleicoes2022&src=typed_query&f=live)
