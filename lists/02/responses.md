# Lista 02 - Inteligência Artificial

* Mariana Almeida Mendonça
* Inteligência Artificial - Profa. Cristiane Neri Nobre.

## Questão 1

### Questão 1.1 

Uma árvore de decisão é gerada por meio de uma hierarquia de melhores atributos, através de calculos matemáticos como de Entropia. O fator da hierarquia é algo muito importante para a definição de uma boa árvore de decisão, visto que a raiz da árvore seja um atributo de grande definição de dados, sendo aquele que vai mais longe no conceito de classificação. 


### Questão 1.2

Considerando que a árvore foi gerada de uma forma correta e com um bom nível de classificação, está árvore pode ser utilizada para classificar novos dados, visto que ela já adquiriu um aprendizado para realizar tal classificação. Outro fator, seria interpretar padrões e compreender o que pode acontecer com novas classificações. 

### Questão 1.3

A principal vantagem da árvore de decisão seria seu fator de interpretabilidade, já que permite tomar decisões complexas por meio de poucas decisões a serem tomadas, além de possuir regras simples que são definidas por mio de ações de `se então`. Já sua desvantagem seria a grande mudança da sua árvore em pequenas alterações, gerando árvores completamente diferentes além de não ser muito útil para grande volume de classes e para atributos não muito relevantes.

### Questão 1.4

Avaliamos a qualidade de uma árvore quando ela apresenta uma profundidade moderada e com uma boa escolha de raiz, que tenha boas classificações em poucos níveis, sendo quantificado por meio do aumento da entropia em cada nível. 

### Questão 1.5

Ao começar pela raiz da árvore iremos encontrar a decisão por meio de cada ramo percorrido, sendo essa registrada como uma regra. Ao fim, quando encontrar um nó folha a regra estará definida, sendo necessário percorrer um novo caminho para encontrar as demais regras. 

## Questão 2

### Questão 2.1 

#### Entropia

* Total de registros: 12
* `Conclusao = Sim`: 6
* `Conclusao = Nao`: 6

$$
\text{Entropia(S)} = -\frac{6}{12}\log_2\frac{6}{12} - \frac{6}{12}\log_2\frac{6}{12} = -0.5 \log_2 0.5 - 0.5 \log_2 0.5 = 1
$$

---

#### Ganho de informação por atributo

##### **1. Alternativo (Sim / Nao)**

| Alternativo | Sim | Nao | Entropia |
| ----------- | --- | --- | -------- |
| Sim         | 3   | 1   | 0.811    |
| Nao         | 3   | 5   | 0.918    |

$$
\text{Ganho(Alternativo)} = 1 - \left(\frac{4}{12}*0.811 + \frac{8}{12}*0.918\right) \approx 0.064
$$

---

##### **2. Bar (Sim / Nao)**

| Bar | Sim | Nao | Entropia |
| --- | --- | --- | -------- |
| Sim | 3   | 2   | 0.971    |
| Nao | 3   | 4   | 0.985    |

$$
\text{Ganho(Bar)} \approx 0.020
$$

---

##### **3. SexSab (Sim / Nao)**

| SexSab | Sim | Nao | Entropia |
| ------ | --- | --- | -------- |
| Sim    | 3   | 2   | 0.971    |
| Nao    | 3   | 4   | 0.985    |

$$
\text{Ganho(SexSab)} \approx 0.020
$$

---

##### **4. Fome (Sim / Nao)**

| Fome | Sim | Nao | Entropia |
| ---- | --- | --- | -------- |
| Sim  | 3   | 2   | 0.971    |
| Nao  | 3   | 4   | 0.985    |

$$
\text{Ganho(Fome)} \approx 0.020
$$

---

##### **5. Cliente (Alguns / Cheio / Nenhum)**

| Cliente | Sim | Nao | Entropia |
| ------- | --- | --- | -------- |
| Alguns  | 3   | 0   | 0        |
| Cheio   | 2   | 2   | 1        |
| Nenhum  | 1   | 2   | 0.918    |

$$
\text{Ganho(Cliente)} = 1 - \left(\frac{3}{12}*0 + \frac{4}{12}*1 + \frac{3}{12}*0.918\right) \approx 0.459
$$

-> **Cliente** é a raiz da árvore (maior ganho).

---

##### **6. Preco (R / RR / RRR)**

| Preco | Sim | Nao | Entropia |
| ----- | --- | --- | -------- |
| R     | 3   | 3   | 1        |
| RR    | 2   | 0   | 0        |
| RRR   | 1   | 3   | 0.811    |

$$
\text{Ganho(Preco)} \approx 0.145
$$

---

##### **7. Chuva (Sim / Nao)**

| Chuva | Sim | Nao | Entropia |
| ----- | --- | --- | -------- |
| Sim   | 3   | 1   | 0.811    |
| Nao   | 3   | 5   | 0.918    |

$$
\text{Ganho(Chuva)} \approx 0.064
$$

---

##### **8. Res (Sim / Nao)**

| Res | Sim | Nao | Entropia |
| --- | --- | --- | -------- |
| Sim | 4   | 2   | 0.918    |
| Nao | 2   | 4   | 0.918    |

$$
\text{Ganho(Res)} \approx 0.083
$$

---

##### **9. Tipo (Frances / Tailandes / Hamburger / Italiano)**

| Tipo      | Sim | Nao | Entropia |
| --------- | --- | --- | -------- |
| Frances   | 1   | 1   | 1        |
| Tailandes | 2   | 2   | 1        |
| Hamburger | 2   | 2   | 1        |
| Italiano  | 1   | 1   | 1        |

$$
\text{Ganho(Tipo)} \approx 0
$$

---

##### **10. Tempo (0-10 / 10-30 / 30-60 / >60)**

| Tempo | Sim | Nao | Entropia |
| ----- | --- | --- | -------- |
| 0-10  | 2   | 2   | 1        |
| 10-30 | 1   | 1   | 1        |
| 30-60 | 1   | 0   | 0        |
| >60   | 2   | 3   | 0.971    |

$$
\text{Ganho(Tempo)} \approx 0.080
$$

---

### Questão 2.2

* **Raiz da árvore:** `Cliente` (ganho ≈ 0.459)

#### Raiz da árvore

* Raiz: **Cliente** (maior ganho ≈ 0.459)

**Ramos:**

* `Alguns` → todos `Sim` → folha → **Sim**
* `Nenhum` → todos `Nao` → folha → **Nao**
* `Cheio` → registros 2,4,5,11 → `Sim`=2, `Nao`=2 → precisamos calcular ganho de informação **dentro desse subconjunto** para escolher o segundo nível.

---

##### ** Subconjunto `Cliente = Cheio`**

Registros:

| Alternativo | Bar | SexSab | Fome | Preco | Chuva | Res | Tipo      | Tempo | Conclusao |
| ----------- | --- | ------ | ---- | ----- | ----- | --- | --------- | ----- | --------- |
| Sim         | Sim | Nao    | Sim  | R     | Nao   | Nao | Tailandes | 10-30 | Sim       |
| Sim         | Sim | Sim    | Sim  | RRR   | Nao   | Sim | Italiano  | 10-30 | Nao       |
| Nao         | Sim | Sim    | Nao  | R     | Sim   | Nao | Hamburger | >60   | Nao       |
| Sim         | Sim | Sim    | Sim  | RRR   | Nao   | Sim | Italiano  | 10-30 | Sim       |

Total: 4 registros → `Sim`=2, `Nao`=2 → entropia do subconjunto = 1

---

#### **Ganho de informação por atributo (dentro do subconjunto)**

##### **Atributo: Alternativo**

| Alternativo | Sim | Nao | Entropia |
| ----------- | --- | --- | -------- |
| Sim         | 2   | 1   | 0.918    |
| Nao         | 0   | 1   | 0        |

$$
\text{Ganho(Alternativo)} = 1 - \left(\frac{3}{4}*0.918 + \frac{1}{4}*0\right) \approx 0.311
$$

---

##### **Atributo: Preco**

| Preco | Sim | Nao | Entropia |
| ----- | --- | --- | -------- |
| R     | 1   | 1   | 1        |
| RRR   | 1   | 1   | 1        |

$$
\text{Ganho(Preco)} = 1 - \left(\frac{2}{4}*1 + \frac{2}{4}*1\right) = 0
$$

---

##### **Atributo: Res**

| Res | Sim | Nao | Entropia |
| --- | --- | --- | -------- |
| Sim | 1   | 1   | 1        |
| Nao | 1   | 1   | 1        |

$$
\text{Ganho(Res)} = 0
$$

---

##### **Atributo: Fome**

| Fome | Sim | Nao | Entropia |
| ---- | --- | --- | -------- |
| Sim  | 2   | 0   | 0        |
| Nao  | 0   | 2   | 0        |

$$
\text{Ganho(Fome)} = 1 - \left(\frac{2}{4}*0 + \frac{2}{4}*0\right) = 1
$$

-> **Fome** é o atributo do **segundo nível** do ramo `Cliente = Cheio`.

