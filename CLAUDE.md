# AMOSTRAGEM — Bolfarine & Bussab, Elementos de Amostragem

Projeto de estudo autodidata de Amostragem (populações finitas).
Toda a produção é **em português (pt-BR)**.

Este projeto é irmão do `ESTOCASTICOS` (Ross), do `MULTI` (Johnson & Wichern)
e do `PP_estudo` (Montgomery): mesma estrutura, mesmo CSS, mesmo formato de
aula. Diferenças: o tema é **azul-cobalto**, e — como no ESTOCASTICOS — há
**três caixas matemáticas coloridas** (resultado / demonstração / exemplo),
com a caixa de resultado em **petróleo** (não índigo, para não brigar com o
azul do tema).

## O livro

- Arquivo: `elementos-de-amostragem.pdf` (1,4 MB, 281 páginas)
- Bolfarine, H.; Bussab, W. O. — **Elementos de Amostragem**, IME-USP, maio de
  2004 (pré-print em pdfTeX; a edição impressa é Blucher, 2005)
- 11 capítulos + apêndices A (palavras-chave, p. 261) e B (tópicos para um
  levantamento, p. 265) + referências

**É um PDF nativo de pdfTeX, sem bookmarks.** A camada de texto existe, mas os
**acentos vêm separados das letras** (“S˜ao”, “Matem´atica”, “¸c˜ao”) e o “i”
acentuado vem como i-sem-pingo + acento. `ferramentas/extrair.py::limpar()`
recompõe tudo; todo comando de texto passa por ela. As fórmulas saem com as
quebras do TeX (frações e somatórios empilhados) — bastam para localizar e
conferir. As tabelas saem com as células em linhas separadas e **os brancos da
Tabela 2.8 (= zeros) somem no texto**: para tabelas numéricas, extrair por
coordenadas com `page.get_text("words")` e atribuir cada número à coluna pela
borda direita (`x1`), como se fez para a Tabela 2.8.

**Offset constante: página do PDF = página do livro + 12.** Use
`livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py` mesmo assim.

| Cap. | Título | Livro p. | PDF p. | Status |
|---|---|---|---|---|
| 1 | Noções básicas | 1 | 13 | ✅ `estudo/cap01/01-00-nocoes-basicas.html` |
| 2 | Definições e notações básicas | 37 | 49 | ✅ `estudo/cap02/02-00-definicoes-e-notacoes-basicas.html` |
| 3 | Amostragem aleatória simples | 61 | 73 | ✅ `estudo/cap03/03-00-amostragem-aleatoria-simples.html` |
| 4 | Amostragem estratificada | 93 | 105 | ✅ `estudo/cap04/04-00-amostragem-estratificada.html` |
| 5 | Estimadores do tipo razão | 127 | 139 | — |
| 6 | Estimadores do tipo regressão | 145 | 157 | — |
| 7 | Amostragem por conglomerados em um estágio | 159 | 171 | — |
| 8 | Amostragem em dois estágios | 197 | 209 | — |
| 9 | Estimação com probabilidades desiguais | 225 | 237 | — |
| 10 | Resultados assintóticos | 239 | 251 | — |
| 11 | Exercícios complementares | 249 | 261 | — |
| A | Relação de palavras-chave | 261 | 273 | referência |
| B | Tópicos para um levantamento amostral | 265 | 277 | referência |

## Preferências de estudo definidas

| Item | Decisão |
|---|---|
| Objetivo | Disciplina de Amostragem. Percurso **desde o cap. 1**, porque o vocabulário (unidade elementar/amostral, populações alvo/referida/amostrada, estrato × subclasse) e a atitude (amostra probabilística, não “representativa”) são cobrados. Ênfase em entender de onde vem cada resultado. |
| Demonstrações | Manter as que agregam: as que passam por `fᵢ`/`δᵢ`, simetria do plano, tamanho fixo, (2.4). Pura álgebra fica resumida na prosa. |
| Caixas | Definições em `.caixa.definicao` (neutra, filete petróleo — é a caixa mais frequente deste livro); resultados/identidades numeradas em `.caixa.teorema` (petróleo, fundo tingido); demonstrações em `.caixa.demonstracao` (verde-musgo); exemplos em `.caixa.exemplo` (âmbar). Avisos em `.caixa.aviso` (castanho-queimado). |
| Exemplos e exercícios | Selecionar os mais relevantes; no cap. 2, **enumerar `S_A` por completo** para cada plano e conferir cada fração. Os exercícios do cap. 1 são de discussão; as respostas são minhas (o livro não traz gabarito). |
| Software | **R**, funções de base. Padrão do cap. 2: `expand.grid`/`combn` para listar as amostras, vetor `p` de probabilidades e somas ponderadas para `E`, `Var`, `Cov`. |
| Formato | **Arquivos HTML locais** em `estudo/`. Offline. Matemática em **MathML nativo** (sem CDN, sem JS). |
| Idioma | Português (pt-BR). Termos técnicos com o original em inglês entre parênteses na primeira ocorrência quando o livro o faz (survey, checklist, peoplemeter). |

## Como trabalhar aqui

**Geração sob demanda, capítulo por capítulo.** A cada sessão o usuário escolhe
o próximo capítulo e eu gero uma página de estudo focada.

### Formato "aula em 12 passos" (refeito em 2026-09-27)

Os capítulos 1 a 4 foram reescritos neste formato, a pedido do usuário, para
leitura com dificuldade de atenção. **Não mencionar isso no texto nem no site.**
Cada decisão de layout responde a um achado da literatura:

| Achado | Peça da página |
|---|---|
| Segmentação — segmentos curtos controlados pelo leitor batem texto corrido (10 de 10 testes, efeito mediano d ≈ 0,79; meta-análise de 88 estudos confirma, com queda de carga cognitiva) | **12 passos numerados**, um por tela: `<h2 class="passo"><span class="n">N</span> título</h2>` + `<p class="marco">Passo N de 12</p>` |
| Sinalização — conclusão antes do desenvolvimento | `.ideia`: uma ou duas frases em corpo grande abrindo o passo |
| *Concreteness fading* — concreto primeiro, símbolo depois, é melhor que o inverso (Fyfe et al.), para quem tem pouca e muita base | `.par` com `.caso` (âmbar, "No exemplo") à esquerda e `.simb` (petróleo, "Em símbolos") à direita, sempre nessa ordem |
| Recuperação ativa — a técnica mais apoiada, com benefício igual para leitores com e sem déficit de atenção | `.checagem`: uma pergunta ao fim de **cada** passo, resposta em `<details>` |
| Mas recall por seções parece melhor na hora (81% × 54%) e rende **menos** dois dias depois (37% × 45%, d = 0,45), com lembrança menos organizada | `.fecho` no fim manda escrever o capítulo **inteiro de uma vez**, e diz por quê; segue a lista `ol.conferir` de 12 itens |
| Redução de carga estranha | frases curtas; contas em `ol.receita`, uma operação por linha |

Estrutura fixa de cada página: topo → `.objetivo` → caixa "Como usar esta
página" → 12 passos → `.fecho` → exercícios resolvidos (carregados intactos da
versão anterior) → `.nota` → `.nav-rodape`.

**Tom:** professor dando aula, não resumo. Frase curta. Explicar o *porquê* e
ligar cada conceito a onde ele reaparece depois. Evitar parênteses encaixados e
orações subordinadas em cadeia — foi o que mais se cortou na reescrita.

**Regra dos números:** todo resultado numérico é *calculado* (Python com
`fractions.Fraction` no scratchpad, para as distribuições amostrais; numpy para
o resto), nunca copiado de memória, e conferido contra o livro. As saídas de R
nas páginas são escritas à mão a partir dos números conferidos em Python —
**R não está instalado no PATH**. Mantê-las simples, com poucas casas. Para
simulações (`rnorm`, `set.seed`) **não inventar saída**: mostrar só o código
e dizer o que esperar.

**Divergências encontradas no livro:**

- Cap. 1, p. 21, exemplo eleitoral: o intervalo para n = 1600 sai impresso
  “53,5% a 59,5%”; o correto é 53,6%–58,4% (meia-largura 2,4 pontos). Anotado
  na `.nota` do cap. 1.
- Cap. 2, Ex. 2.7: a fórmula de `P(s)` repete “se i ∈ s” por erro de
  composição; leia “1/9 se s ∈ S₂”. Anotado.
- Cap. 2, Ex. 2.14: EQM impresso 0,6458 (viés arredondado 0,13 ao quadrado);
  exato 97/150 = 0,6467. Anotado.
- Cap. 3, Ex. 3.2: o erro máximo do livro é **B = √2** (daí D = 2/2² = 0,5 e
  n = 48/0,5 = 96). A primeira versão da aula transcreveu "B = 2", que daria
  n = 48 — corrigido em 2026-09-27. Com z = 1,96, n = 93.
- Cap. 3: nos tamanhos de amostra o livro usa z ≈ 2 (D = B²/4) e nos
  intervalos 1,96 (Ex. 3.2: n = 96 com z = 2, 93 com 1,96; Ex. 3.6: 3466 vs
  3341). Segui o livro nos exemplos, 1,96 nos exercícios. Ex. 3.3: limite
  inferior −0,061, impresso 0,00. Ex. 3.9(c) fala em "residentes" (herança do
  3.4); tomei Y > 3. Ex. 3.6: o estimador pedido é viesado (E = 4 ≠ 4,5).
- Cap. 4, (4.19): impresso com os dois fatores iguais a Σ W_h σ_h/√c_h; o
  correto é (Σ W_h σ_h √c_h)(Σ W_h σ_h/√c_h)/V_es. Anotado. Ex. 4.1 dá S²_h e
  as fórmulas AASc pedem σ²_h: converti por (N_h − 1)/N_h.

**Numeração de equações do cap. 4 — conferida contra o PDF em 2026-09-27**
(errei nisto na primeira versão do guia de prova; já corrigido): (4.18) é o n
com C′ fixado; (4.19) o n com V_es fixado; (4.20) Neyman; (4.21) V_ot;
(4.22) V_pr = σ²_d/n; (4.23) Nσ² = ΣN_hσ²_h + ΣN_h(μ_h−μ)²; (4.24)
V_pr − V_ot = σ²_dp/n; (4.25) V_c = V_ot + σ²_e/n + σ²_dp/n. A desigualdade
V_ot ⩽ V_pr ⩽ V_c **é o Teorema 4.4 e não tem número de equação** — citar
“(4.23)” para ela é erro. Idem (4.5), que é sobre as v.a. y_h1,…,y_hn_h e não
sobre Var[ȳ_es]. Ao citar equação, confira com uma varredura do texto das
páginas por linhas que sejam exatamente “(N.N)”.

**Números conferidos que valem reutilizar:** Tabela 2.8 (180 condomínios):
τ_Y = 3363, μ_Y = 18,683, S²_Y = 409,75; τ_X = 4928, μ_X = 27,378,
S²_X = 609,41; P(Y > 20) = 58/180; ρ_XY = 0,962; R = 0,6824. Os vetores `Y` e
`X` em R estão no Exercício 2.2 do cap. 2 — copiar de lá para os caps. 3, 5 e 6.
Exercício 1.2: o livro tem 58 500 palavras nas 269 páginas numeradas (critério:
token com ao menos uma letra, no texto do PDF).
Tabela 2.8 por estratos de 60 (ordem da lista): μ_h = 28,57, 20,80, 6,68;
σ²_h = 544,8, 326,3, 105,1; σ²_d = 325,4, σ²_e = 82,1 (Ex. 4.9).
População do Ex. 4.1 (D = 13,17,6,5,10,12,19,6): μ = 11, σ² = 24, S² = 192/7.
**Amostras "sorteadas" nos exercícios 3.9 e 4.9:** índices gerados em Python
(`numpy.random.default_rng(2004)`, `integers(1, 181, n)`) e listados
explicitamente no código R da página — reproduzível sem R.

**Ganchos plantados (retomar quando o capítulo chegar):**

- estimador expansão `T = nȳ + (N − n)ȳ`: "a parte não observada é estimada
  por ȳ" → razão e regressão substituem ȳ por uma previsão, **caps. 5 e 6**
- Ex. 3.7 (dentistas) = pós-estratificação / estimador razão com X = 140
  conhecido → **cap. 5**; Ex. 3.5/3.41 (`ȳ_c`) = usar informação auxiliar
  bate ȳ fora da classe linear → **caps. 5 e 6**
- `r` viesado, `E[f̄]` não viesada só em planos simétricos → **cap. 5**
- Ex. 4.6/4.27: `ȳ_m` (média simples de amostra estratificada) é viesado; o
  Ex. 3.6 é um caso → pesos amostrais, **caps. 8 e 9**
- EPA (cap. 3, `(N−n)/(N−1)`; cap. 4, `1 − σ²_e/σ²`) → perda dos conglomerados
  e correlação intraclasse, **cap. 7**
- Ex. 4.16 (estágios dentro de estratos, PPT) ficou de fora — retomar no
  **cap. 8/9**
- correlação intraclasse mencionada nos exercícios 1.10 e 1.12 → **cap. 7**
- `π_i`, `π_ij`, e o `π_13 = 0` do plano E → Horvitz–Thompson, **cap. 9**
- (2.19)–(2.20) (esperança e variância iteradas) → **cap. 8**
- sistemático como conglomerado único, sem estimativa de variância → **7.8**

## Ferramentas

`ferramentas/extrair.py` — localiza o PDF sozinho na raiz (prioridade ao nome
que contém "amostra"), recompõe os acentos (`limpar`) e converte a numeração
com `livro2pdf`/`pdf2livro`. Redirecionar a saída de `texto` para arquivo
quebra no Windows (`cp1252`): use `PYTHONIOENCODING=utf-8`. `sumario` avisa
que o PDF não tem bookmarks (o sumário impresso está nas PDF p. 3–7).
`ferramentas/figuras.py` — copiado do ESTOCASTICOS; aglomera os traçados
vetoriais da página em caixas.

```bash
python ferramentas/extrair.py texto --livro 61 92
python ferramentas/extrair.py recorte 22 186 128 514 613 fig.png
python ferramentas/extrair.py buscar "Neyman"
python ferramentas/figuras.py listar 22
```

Dependências: `pymupdf` (instalado). Python 3.13.

Figuras: o cap. 1 tem três. A Fig. 1.1 (PDF p. 22, recorte `186 128 514 613`)
foi recortada; as Figs. 1.2 e 1.3 são árvores desenhadas com `\put` do TeX e
saem como lixo no texto — foram **redesenhadas em SVG** com as classes `.cx`,
`.cx-folha`, `.ramo`, `.tx`, `.tx-crit` de `estilo.css`. Cap. 2 não tem
figuras, só tabelas (refeitas em HTML). Cap. 3 idem. Cap. 4 só tem a Tabela
4.1; desenhei em SVG a população do Ex. 4.1 com `<tspan baseline-shift="sub">`
para os subíndices.

## Folha de consulta (guia de prova)

Além das aulas há **duas folhas de consulta** para levar impressas na prova,
ambas cobrindo os capítulos 1 a 4 num só documento, 5 páginas A4 cada:

| Arquivo | O que é |
|---|---|
| `estudo/guia/01-04-guia-de-prova.html` | o guia “de trabalho”: mapa de decisão, enunciados, exemplos numéricos, receitas, “fato ou fake”, checklist, fórmulas de bolso, R, glossário |
| `estudo/guia/01-04-definicoes-e-resultados.html` | só os enunciados: toda definição, teorema, corolário e lema, **com as hipóteses de cada um**, e um quadro final “resultado × o que exige × quando quebra” |

O molde veio do `ESTOCASTICOS` (`estudo/cap04/04-99-guia-de-prova.html`); lá é
uma folha por capítulo, aqui uma folha por bloco de capítulos, porque foi o
pedido: “os capítulos 1 a 4 num mesmo PDF”.

**Ela não usa `estilo.css`.** Carrega `tema.css` + **`assets/guia.css`**
(copiado do ESTOCASTICOS sem mudar estrutura — as cores vêm todas do tema, e
por isso a mesma folha sai em cobalto aqui e em índigo lá): uma coluna na tela,
`columns: 2` A4 na impressão, corpo 8,2 pt. Cinco caixas, cada uma com
`--cor`/`--cor-fundo` próprias:

| Classe | Cor | Uso |
|---|---|---|
| `.bloco.teo` | petróleo | definição, teorema, corolário, quadro-resumo |
| `.bloco.dem` | verde-musgo | por que é verdade (demonstração curta) |
| `.bloco.ex` | âmbar | exemplo numérico de fixação |
| `.bloco.rec` | azul-cobalto | receita: passo a passo para a prova |
| `.bloco.arm` | castanho | armadilha, “fato ou fake”, erro clássico |
| `.bloco.def` | azul-acinzentado, neutro | definição (acrescentada aqui; definição é texto de referência, não resultado a destacar — mesma regra de `.caixa.definicao` nas aulas) |

O título da caixa é um `<h4>` (barra sólida, texto em `--menu-texto`). Outras
peças: `.chave` (destaque cobalto inline), `.miudo` (corpo menor), `.rot-e` /
`.rot-s` (Enunciado./Solução.), `.qed`, `.so-tela` (aviso que some no papel),
`.legenda` (a tira de cores do cabeçalho), `.eq .num` (número da equação),
`pre .cmt` / `pre .out` (comentário e saída do R).

**Conteúdo do guia de prova:** mapa de decisão “o que a questão pede × que
ferramenta usar” → cap. 1 (objetivo→parâmetro, três unidades, três populações,
estrato × subclasse, representativa × probabilística, 8 passos, erros) → cap. 2
(parâmetros, `fᵢ`/`δᵢ`, plano, (2.14)–(2.15), viés/EQM, `πᵢ`) → cap. 3 (AASc ×
AASs numa tabela, por que `(1−f)`, IC, tamanho da amostra, proporções,
otimalidade) → cap. 4 (decomposição, Teor. 4.1, as quatro alocações, Neyman por
Cauchy–Schwarz, (4.23)–(4.25), IC, proporções) → fato ou fake → checklist →
fórmulas de bolso → R → glossário de símbolos. Poucos exercícios, muitos
exemplos curtos — é folha de consulta, não lista.

**Conteúdo da folha de definições e resultados:** cap. 1 (o vocabulário, que o
livro não numera) → Definições 2.1–2.11 e as identidades (2.2)–(2.20) → cap. 3
(Teoremas 3.1–3.10, Corolários 3.1–3.5, Definição 3.1, Lema 3.1, equações
(3.1)–(3.35)) → cap. 4 (Teoremas 4.1–4.6, Corolários 4.1–4.5, equações
(4.1)–(4.33)) → quadro das hipóteses. **Toda caixa abre com uma linha
“Hipóteses:”** — foi o pedido explícito. A lista do que existe numerado saiu de
uma varredura do PDF com o padrão
`(Definição|Teorema|Corolário|Lema|Proposição) NN.NN` sobre as págs. 1–126;
vale repetir a varredura ao estender para o cap. 5.

### Gerar o PDF

O Chrome está instalado e imprime sem abrir janela:

```bash
python -m http.server 8765     # ou o .claude/launch.json
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu   --no-pdf-header-footer --print-to-pdf="C:\Users\gabri\OneDrive\Desktop\AMOSTRAGEM\estudo\guia\01-04-guia-de-prova.pdf"   "http://localhost:8765/estudo/guia/01-04-guia-de-prova.html"
```

Duas armadilhas já pagas: o endereço precisa ser **http://** (o CSS relativo
não carrega no headless a partir de `file://`), e o `--print-to-pdf` precisa de
**caminho absoluto no estilo Windows** — com caminho relativo do Git Bash o
Chrome responde “O sistema não pode encontrar o caminho especificado”.

Gere as duas folhas trocando o nome do arquivo. Os PDFs ficam **fora do git**
(`*.pdf` no `.gitignore`): são artefatos derivados. Gerar as duas em sequência
por um laço do Bash é onde se erra — `"$B\\$n.pdf"` não expande a
variável e o Chrome escreve um arquivo chamado `guia$n.pdf` na pasta errada.
Faça o laço em Python (`subprocess.run([chrome, ...])`) ou escreva os dois
comandos por extenso.

**Armadilha da impressão:** no papel nada rola. `overflow-x: auto` (código,
`.rolagem`, `math[display="block"]`) vira *conteúdo cortado* no PDF. O
`@media print` do `guia.css` já neutraliza os três, mas equação ou linha de
código larga demais continua vazando — a correção é quebrar em duas linhas,
não mexer no CSS. Confira sempre com pymupdf, página a página: além de ler as
imagens, vale checar por coordenada se algum bloco passa da margem direita
(595 − 22,7 pt) ou atravessa a calha entre colunas (290 → 305 pt).

**Parênteses do MathML:** `<mo>(</mo>` é *stretchy* por padrão, e em
`math[display="block"]` isso estica `n(s)`, `P(s)`, `E[t]` até ficarem enormes.
A correção é `<mo stretchy="false">` **só** onde o conteúdo é baixo — um script
que casa cada par `( )`, `[ ]`, `{ }` e mantém o esticamento quando encontra
`mfrac|msqrt|munder|munderover|mover|mtable|msup|msubsup|mroot` dentro dele.
Já aplicado nas duas folhas.

## Convenção de nomes

Igual ao MULTI. **Números sempre com dois dígitos**, minúsculas, sem acento,
hífen entre palavras.

| O quê | Padrão | Exemplo |
|---|---|---|
| Pasta do capítulo | `capNN/` | `cap02/` |
| Página do capítulo inteiro | `NN-00-titulo.html` | `cap02/02-00-definicoes-e-notacoes-basicas.html` |
| Figura | `img/fig-NN-MM.png` | `cap01/img/fig-01-01.png` |
| Folha de consulta | `guia/NN-MM-<assunto>.html` (dos caps. NN a MM) | `guia/01-04-guia-de-prova.html` |

Ao criar uma aula nova, acrescentar o link em **três** lugares de
`estudo/index.html` (a folha de consulta está nos mesmos três, mais um bloco
“Folha de consulta” na barra lateral e uma menção no subtítulo): a lista da barra lateral (trocar o `<li class="adiante">`
por um `<li>` com link), o cartão em "Aulas disponíveis" (trocar o
`<span class="cartao pendente">` por `<a class="cartao">`) e a linha da tabela
da seção **"Menu"**. E acertar o `.nav-rodape` (anterior/próxima) da aula
vizinha — o do cap. 4 hoje diz "Cap. 5 … (em breve)" sem link.

## Layout das páginas

O CSS está separado em dois arquivos e essa separação é para valer:

- `estudo/assets/tema.css` — **única** fonte de cores, fontes e medidas, com
  bloco `@media (prefers-color-scheme: dark)`. Tema: **azul-cobalto**. Regra
  geral: superfícies neutras, cor só em tipografia e filetes. **Exceção:** as
  variáveis `--teorema/--teorema-fundo` (petróleo), `--demo/--demo-fundo`,
  `--exemplo/--exemplo-fundo` dão fundo tingido às três caixas matemáticas.
  `--ambar` (avisos) aqui é castanho-queimado, porque o âmbar de verdade ficou
  para os exemplos.
- `estudo/assets/estilo.css` — só estrutura, copiado do ESTOCASTICOS e
  acrescido das classes de árvore para SVG: `.cx` (nó destacado), `.cx-folha`
  (nó neutro), `.ramo` (traço sem seta), `.tx`, `.tx-crit`. **Nunca escrever
  cor literal aqui.**
- `estudo/assets/aula.css` — **camada do formato em passos**, carregada
  *depois* de `estilo.css` nas quatro aulas. Só acrescenta; não redefine nada
  do que já existia. Peças: `h2.passo`/`.n`, `.marco`, `.ideia`, `.par` com
  `.caso`/`.simb`, `ol.receita`, `.checagem`, `.chip`, `.fileira`, `.numerao`,
  `.miudo`, `.fecho`/`ol.conferir`, e os complementos de SVG `.tx-rot`,
  `.barra`, `.barra-alvo`, `.eixo`. Cor nenhuma literal, como sempre.

O `<head>` de toda página de aula:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Cap. N — Título</title>
<link rel="stylesheet" href="../assets/tema.css?v=1">
<link rel="stylesheet" href="../assets/estilo.css?v=1">
<link rel="stylesheet" href="../assets/aula.css?v=1">
```

Tudo o mais (grade de quebra de coluna, `.topo + .objetivo`, barra lateral
fixa com `<details class="sub">`, `h3` com `id="{h2}-{k}"`, `td.txt`,
`?v=` a incrementar ao mexer no CSS) é idêntico ao MULTI/ESTOCASTICOS.

**MathML — armadilhas já encontradas:**

- Espaço nas bordas de `<mtext>` é descartado. Use `<mspace width="0.35em"/>`
  fora do `<mtext>`.
- `<mfrac linethickness="0">` para coeficientes binomiais.
- `<mo>(</mo>` é **stretchy** por padrão, e em `math[display="block"]` isso
  estica `n(s)`, `P(s)`, `E[t]` até ficarem enormes. Use
  `<mo stretchy="false">` quando o conteúdo entre os delimitadores for baixo —
  e **só** nesse caso: em volta de `mfrac`, `msqrt`, `munder`, `mover`,
  `msup` etc. o esticamento é o certo.
- **Equações em bloco com mais de ~700 px estouram a coluna de leitura** (46rem)
  e viram rolagem horizontal. Regra: no máximo duas igualdades por
  `<math display="block">`; a cadeia longa da demonstração de (2.15) foi
  partida em dois blocos. Conferir com JS no preview:
  `[...document.querySelectorAll('math[display=block]')].filter(m => m.scrollWidth > m.clientWidth + 1)`.
**SVG — armadilhas do formato novo:**

- `.tx-rot` (o rótulo curto dos diagramas) tem `text-transform: uppercase`.
  **Nunca pôr símbolo matemático dentro dele**: `n = 2` vira `N = 2` e `r` vira
  `R`, que são outros parâmetros. Reescrever o rótulo em palavras.
- Texto de SVG **não herda** a cor do corpo: toda classe nova precisa de `fill`
  explícito, ou o rótulo sai preto no modo escuro.
- Subíndices com `<tspan baseline-shift="sub" font-size="8.5">`; escrever
  `f i` com espaço sai feio e é o que acontece se esquecer.

- Um `Write` só não cabe: cada aula tem 640–920 linhas. Escrever em três partes
  no scratchpad e concatenar com `cat`; validar o aninhamento com o
  `valida.py` (html.parser) a cada passada. **Heredocs no Bash quebram com
  conteúdo HTML longo** (aspas/contra-barras): usar o `Write` para os HTML.

## Preview local

O painel de navegador do Claude Code serve `file://` como snapshot (`data:`) e
não carrega o CSS relativo. Use `.claude/launch.json` (fora do git), que sobe
`python -m http.server 8765`, e abra
`http://localhost:8765/estudo/cap02/02-00-definicoes-e-notacoes-basicas.html`.
As capturas de tela falham depois de rolar a página (janela oculta); para
inspecionar os SVG, serializar com estilos computados e desenhar num canvas
via `javascript_tool`, salvando o PNG no scratchpad.

## Estrutura

```
AMOSTRAGEM/
├── elementos-de-amostragem.pdf   (fora do git: .gitignore)
├── index.html              redireciona para estudo/ — serve ao GitHub Pages
├── README.md               documentação pública do repositório
├── CLAUDE.md               este arquivo
├── .gitignore  .gitattributes  robots.txt
├── ferramentas/
│   ├── extrair.py
│   └── figuras.py
└── estudo/
    ├── index.html          painel com o percurso
    ├── assets/
    │   ├── tema.css        cores, fontes, medidas (azul-cobalto)
    │   ├── estilo.css      estrutura e layout das aulas
    │   ├── aula.css        formato "12 passos" (carrega depois de estilo.css)
    │   └── guia.css        layout da folha de consulta (A4, 2 colunas)
    ├── cap01/
    │   ├── 01-00-nocoes-basicas.html
    │   └── img/fig-01-01.png
    ├── cap02/
    │   └── 02-00-definicoes-e-notacoes-basicas.html
    ├── cap03/
    │   └── 03-00-amostragem-aleatoria-simples.html
    ├── cap04/
    │   └── 04-00-amostragem-estratificada.html   (diagrama SVG da população do Ex. 4.1)
    └── guia/
        ├── 01-04-guia-de-prova.html            guia de trabalho
        ├── 01-04-definicoes-e-resultados.html  só enunciados + hipóteses
        └── *.pdf                               (fora do git: Chrome headless)
```

O repositório está em <https://github.com/GABELCHIOR/AMOSTRAGEM> (remoto
`origin`, branch `main`). O PDF fica de fora pelo `.gitignore`. Para o GitHub
Pages servir o site, ativar em Settings → Pages → branch `main`, pasta `/`
(raiz); a `index.html` da raiz redireciona para `estudo/`.

## Progresso

**Capítulos 1 a 4 prontos** (caps. 1–2 em 2026-09-11; caps. 3–4 em
2026-09-21), **reescritos no formato de 12 passos em 2026-09-27** — as versões
antigas foram substituídas, não há cópia no repositório (o histórico do git
tem). E as **duas folhas de consulta dos caps. 1–4** (guia de prova em
2026-09-22; definições e resultados em 2026-09-27; 5 páginas A4 cada), que
continuam no formato denso original — folha de consulta não é aula.
**O capítulo 5 em diante nasce direto no formato de 12 passos.** Próximo: capítulo 5 (Estimadores do tipo razão, livro 127–144,
PDF 139–156). Ao gerar, retomar: a leitura "parte não observada" do estimador
expansão (cap. 3, seção 2.2); o Ex. 3.7 dos dentistas como razão com X
conhecido; a Tabela 2.8 (ρ_XY = 0,96, R = 0,682) é a população natural para
comparar razão × expansão; Tabela 5.1 do livro enumera `S_AASc` como o cap. 3
— refazer com `expand.grid`. O cap. 6 (regressão) segue o mesmo molde.
