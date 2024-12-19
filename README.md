# Design pattern **Observer**
> ### Conteúdo: Python, POO, SOLID(S), Callback.
<!-- > - **Conteudo didatico** -->

Neste repositório temos um script em Python que irá lhe ajudar a entender o design pattern Observer. Você deve seguir o passo a passo de implementação descrito nesse README.md.
> <sub>O Observer é um padrão de projeto comportamental que permite que você defina um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando (Refactoring.Guru, 2024).</sub>

## Descrição:
O Observer se divide em duas classes principais: **Observer (observador)** e **Subject (sujeito)**. Sua ideia principal concentra-se em criar uma mecânica de **Broadcast** entre as classes que o nosso Subject notifica todos os seus Observers das eventuais mudanças que importam para elas. 

>Sua ideia central gira em torno dessas duas classes mencionadas anteriormente.
```py
# Subject (Sujeito)
class Subject():
    def __init__(self): 
    def subscribe(self): # Adiciona um observador.
    def unsubscribe(self): # Remove um observador.
    def notify(self): # Notifica todos os observadores.

# Observer (Observador)
class Observer():
    def __init__(self):
    def update(self): # Recebe notificações do subject.
```
> FAQ:<br>
> - <sub> **Quando devo usar o pattern Observer?**<br>
> Quando você possui objetos que precisam saber o estado de algo como no caso de canais no YouTube onde todos os inscritos que ativaram o sininho precisam saber quando saiu um vídeo.</sub>
>
> - <sub> **Quais são as vantagens do Observer?**<br>
> Algumas das vantagens são: Centralização de eventos, permitindo os observadores respondam automaticamente a mudança no estado do objeto observado e; Fácil manutenção, já que mudanças no objeto observado não afetam os observadores diretamente, vice-versa.</sub>

## Sobre o script:
Esse código é focado no entendimento do design pattern **Observer**, por isso ele pode desconsiderar alguns fatores como a escalabilidade, já que se pode notar que se um novo funcionário for contratado ele não herdará a base salarial atual dos funcionários com base nos cargos. Então, entenda que ele é assim por que precisa ser simples, para quem o está estudando e isso deixa algumas coisas como escalabilidade e proposito subentendidos pelo usuário que visita esse repositório. Afinal de contas o assunto **Design pattern** não é um tópico para iniciantes, e sim para desenvolvedores que já possuem uma leva conhecimentos em programação, por isso, já se espera que ele entenda as partes subentendidas mencionadas anteriormente.

***Também desconsideramos as heranças das classes porque, como já dito, é esperado que os visitantes desse repositório tenham alguma noção prévia de como aplicá-las com base no exemplo de código apresentado nesse repositório.***

## Passo a passo:
#### 1. Crie a classes Observer com os seguintes Métodos:
|Nome|Observer|
---|---
**Método**|update|
#### 2. Defina o comportamento esperado do Observer ao ser notificado pelo Subject no Método update.
> <sub> **Apenas defina o comportamento sem se preocupar com o Subject.** De inicio, experimente coisas mais simples como mudar um atributo de **False** para **True**; por exemplo, um objeto que se chama "usuário" e mude o atributo "banido" de **False** para **True**.<sub>


#### 3. Crie a classes Subject com os seguintes Métodos.
|Nome|Subject|
---|---
***Atributo***|list_observers
**Método**|subscribe|
**Método**|unsubscribe|
**Método**|notify|
> <sub> **list_observers:** Guarda todas as suas instâncias (Objetos) em uma lista para ser iterada (Percorrida) no Método notify.<br>
> **subscribe:** Adiciona uma instância no list_observers.<br>
> **unsubscribe:** Remove uma instância no list_observers.<br>
> **notify:** Itera todos os objetos no list_observers para chamar o Método update de cada um deles.</sub>
#### 4. No notify, crie um "For" para iterar o atributo "list_observers", assim, podendo chamar o Método "update" de cada um de seus "observers".
```py
# Subject (Sujeito)
class Subject():
    def __init__(self):
        self.list_observers = []
    def subscribe(self): # Adiciona um observador.
    def unsubscribe(self): # Remove um observador.
    def notify(self): # Notifica todos os observadores.
        for observer in self.list_observers:
            observer.update()
```
> - <sub> É importante entender que o **"self.list_observers = [ ]"** não vai sobrecarregar a sua memória pois ele não cria copias das suas instâncias/Objetos para armazenar, ele apenas guarda o endereço de memória que aponda para aquele objeto.</sub> 
> - <sub> O ideal seria fazer com que essas classes fossem herdadas por outras classes para que esse comportamento não precise ser refeito do zero em novas features/classes. Dito isso, qualquer outra classe poderá se tornar um Observer ou Subject.</sub>
### Sugestões:
- Crie um **Método** no subject chamado **unsubscribeAll** para remover todos os observer listados no subject.
- Crie um **Método** no subject chamado **check** para retornar valores que importam para mudanças de comportamento dos **observers**.
- Recomendo que você possua alguma experiência na aplicação desse pattern quando for implementá-lo em algum projeto sério, então, pratique alguns exemplos simples para que você entenda a natureza de sua implementação.
- As mudanças no comportamento devem ser feitas diretamente no Observer, não via notificações.
- O ideal é que o dever do metodo ***notify*** seja apenas notificar para não ferir os principios do **SOLID**(S:Princípio da Responsabilidade Única) considere esse metodo o mais sensivel a essa regra do **SOLID**.
  
<sub>Isso por que o número de iterações vai implicar em uma somatória de vezes em que seu código terá uma chance de quebrar, pois se alguma instância seguir alguma regra especial ou tiver um if muito específico as chances de alguma instância quebrar o seu código são muito consideráveis já que você esta mudando a regra de comportamento por notificação e não a regras do próprio Observer e isso pode te levar a caçar o problema instância por instância.</sub>
> - <sub>Mudança de comportamento no ***notify*** diz respeito a todas a instâncias do subject, então, se algo não esta sendo esperado por alguma instância o código quebra.</sub>
> - <sub>Se a mudança de comportamento for feita no **update**, cada classe saberá como tratar suas condições individualmente.</sub>

<!-- **Vinicius da Silva Ferreira:** Desenvolveu o script de exemplo, documentação e a didatica do material apresentado.-->
