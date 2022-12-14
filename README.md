# 주제
Graph Centrality를 이용한 프로듀서와 아티스트 간 영향력과 음원 성적 분석 및 신곡 추천<br/><br/>

## 구성원
|      이름       |      학과       |학번                          |이메일                          |
|----------------|----------------|-------------------------------|-------------------------------|
|김건희|컴퓨터공학과|2017103958            |tahm_kench@khu.ac.kr            |

<br/>

## 요약
그래프 중심성(Graph Centrality)을 이용해 음원차트에 따른 국내 음악시장에서의 프로듀서와 아티스트 간의 사회연결망을 확인하고, 프로듀서와 아티스트의 각 관계가 어떤 영향을 끼치며 어떠한 상호관계가 존재하는지 분석한다. 이것을 토대로 신곡 중 높은 순위를 차지할 가능성이 있는 음악을 선별하는 것을 목표로 한다.
<br/><br/>

## 연구 배경
최근 음원차트를 봤을 때 발견할 수 있는 점은 유명한 아티스트의 노래가 무조건 높은 순위를 차지하지 않는다는 점이다. 많은 사람에게 익숙한 가수인 ‘트와이스’의 신곡 ‘Talk and Talk’은 발매한 지 약 한 달 뒤인 9월 20일 기준 인기 차트에서 32위를 차지하고 있다. 그에 반하여 상대적으로 인지도가 적은 ‘김승민’의 ‘내 기쁨은 너가 벤틀리를 끄는 거야’는 발매된 지 1년이 넘었지만, 인기차트 27위에 자리 잡고 있다. 이외에도 발매 시기와 관계없이 유명세가 상대적으로 낮은 아티스트의 곡들을 인기차트에서 쉽게 찾아볼 수 있다.<br/>
일반적으로 우리는 아티스트가 곡의 흥행을 좌우한다고 생각하는 경향이 있다. 그러나 위에서도 알 수 있듯이 꼭 그런 것만은 아니며 프로듀서도 아티스트에 못지않은 영향력을 끼친다. <br/>
이에 따라 본 프로젝트에서는 국내 음악의 다양한 분야에서 아티스트뿐만 아니라 프로듀서의 영향력이 음원 성적과 얼마나 긴밀한 연관이 있는지 Graph Centrality를 이용해 분석하고, 아티스트와 프로듀서 간의 상호 관계에 대해서도 연구한다. 이를 기반으로 신곡을 추천해주는 것까지 나아갈 예정이다.<br/>

<br/>

## 관련 연구
### Graph Centrality
그래프 중심성이란 그래프 혹은 사회 연결망에서 꼭짓점 혹은 노드의 상대적 중요성을 나타내는 척도이다. 이 중심성은 지수로 계산되는데, 중점으로 두는 기준에 따라 출력되는 결괏값이 다르다. <br/>
노드들 사이의 최단 경로를 가지고 계산하는 매개 중심성(Betweenness Centrality), 그래프의 노드와 다른 모든 노드 사이의 최단 경로 길이 합의 역수를 이용해서 구하는 근접 중심성(Closeness Centrality), 한 노드에 연결된 모든 엣지의 개수로 중심성을 평가하는 연결 중심성(Degree Centrality) 등 이 밖에도 다른 계산 방법들이 다양하게 존재한다[1].<br/>


### Graph Centrality를 이용한 국내 힙합 프로듀서와 아티스트 간 영향력과 음원 성적 분석
해당 연구에서는 Graph Centrality 중 가중연결 중심성(Weighted Degree Centrality)을 이용해 힙합 장르에서 각 아티스트와 프로듀서의 영향력을 파악하였고, 이를 토대로 음원 성적 사이의 연관성을 분석했다.<br/>
각 엣지에는 음원 성적을 기반으로 가중치를 부여해 중심성을 도출해 시각화하였다. 그 결과, 해당 연도 힙합 장르에서 어떤 아티스트와 프로듀서가 높은 영향력을 끼쳤는지 파악할 수 있었다. 아티스트는 프로듀싱까지 직접 하는 사람이 높은 영향력을 보였고, 프로듀서는 같은 회사 소속의 아티스트와 작업할 때 높은 영향력을 보였다[2].<br/>

<br/>

## 프로그램 및 모듈 설치
#### 1. Web Crolling
```
pip install selenium
pip insatll beautifulsoup4
```
웹 크롤링을 위하여 selenium과 beautifulsup4를 설치한다.

```
https://chromedriver.chromium.org/downloads
```
해당 주소에서 자신의 크롬 버전에 맞는 크롬드라이버를 설치받는다.<br/>


#### 2. Graph
```
pip install pandas
pip insatll networkx
```
그래프 생성을 위하여 pandas와 networkx를 설치한다.


#### 3. Gephi
```
https://gephi.org/
```
그래프 분석을 위하여 Gephi 홈페이지에서 Gephi를 다운로드 받는다.<br/><br/>

## 연구의 중요성/독창성
일반적으로 아티스트가 음원의 흥행을 좌우한다고 생각하지만, 프로듀서도 아티스트 못지않게 음원의 흥행을 좌우한다. 그러나 Graph Centrality를 이용하여 아티스트와 프로듀서를 모두 고려하였던 연구가 이전에는 존재하지 않았다. <br/>
해당 연구를 통하여 아티스트와 프로듀서의 영향력을 파악하는 것뿐만 아니라 음원 순위 예측까지 할 수 있고 그것들을 기반으로 음원 흥행을 위한 전략을 제공할 수 있다.<br/><br/>
![논문](https://user-images.githubusercontent.com/30266366/204955183-4dd77fb8-ec21-4ab6-8f75-1bd43dc23d64.png)<br/>
실제 해당 연구는 KSC 2022에 뽑혀서 논문 등재가 될 예정이며, 12월 말 발표도 진행할 예정이다.<br/>

<br/>

## 연구 목적
해당 연구의 목표는 크게 두 가지다. 첫 번째, Graph Centrality를 이용해 여러 장르에서 프로듀서와 아티스트의 영향력과 관계를 파악한다. 두 번째, 그렇게 파악한 영향력을 바탕으로 아티스트나 프로듀서에게는 음원 성공을 위한 전략을 제공하고, 소비자들에게는 신곡 중 음원 차트에서 높은 순위를 기록할 가능성이 있는 노래를 추천하여 준다.<br/><br/>

## 데이터 추출 및 정제
![크롤링과정](https://user-images.githubusercontent.com/30266366/204949666-b506ded1-c27a-47a8-94ce-abe387c929dd.png)<br/>
데이터 분석에 필요한 데이터는 국내 최대 음원 사이트인 멜론에서 이용하였다. 월간 차트를 이용하여 2019년부터 2021년까지의 댄스, 힙합, 인디 분야의 차트 데이터를 크롤링하였다. 이후 각 장르와 적합하지 않은 곡들을 제외하는 정제 작업을 진행하였으며, 프로듀서 정보는 저작권협회에서 수집을 진행하였다.<br/><br/>

## 그래프 생성
수집한 데이터를 분석하기 위해 ‘그래프’를 이용했다. 아티스트와 프로듀서를 노드로 설정하고, 같은 곡을 작업한 아티스트와 프로듀서를 엣지로 연결하였다. 그리고 엣지에는 음원차트를 기반으로 한 가중치를 부여하였다. 가중치 공식은 먼저 (가중치1)=[(1-(해당 곡의 순위/101)^2)*100]로 설정하였다. 이를 바탕으로 작성된 전체 아티스트와 프로듀서의 엣지의 가중치 중 최대, 최솟값을 구하고 나서 (가중치2)=(가중치1-최솟값)/(댓대값-최솟값)의 식으로 가중치를 계산한다. 마지막으로 각 두 노드 간 협업 된 곡들의 가중치2 값을 총합하여 최종 가중치를 구한다[2]. 가중연결 중심성(Weighted Degree Centrality), 고유벡터 중심성(Eigenvector Centrality)을 이용할 때는 해당 가중치를 그대로 사용하고, 매개 중심성(Betweenness Centrality), 근접 중심성(Closeness Centrality)을 사용할 때는 해당 가중치의 역수를 이용한다.<br/><br/>

![그림1](https://user-images.githubusercontent.com/30266366/204951849-e151cf11-5801-4923-b504-aca9e49690b6.png)
<br/>
Gephi에서 그래프를 시각화한 결과이다.
<br/><br/>


## 중심성 선정
적합한 중심성 선정을 위하여 수집한 데이터에 대하여 매개 중심성(Betweenness Centrality), 근접 중심성(Closeness Centrality), 가중연결 중심성(Weighted Degree Centrality), 고유벡터 중심성(Eigenvector Centrality) 네 가지 중심성을 이용한 분석을 진행하였다. <br/>
힙합 장르는 ‘한국 힙합 어워즈’를 이용하여 올해의 아티스트, 올해의 프로듀서 두 가지 부분의 후보들의 중심성 순위 평균을 계산한 결과 아티스트는 가중연결 중심성(Weighted Degree Centrality)을, 프로듀서는 매개 중심성(Betweenness Centrality)을 사용하였을 때 가장 높은 정확도를 보였다.<br/>
 댄스 장르는 ‘Mnet 아시안 뮤직 어워드’를 이용하였는데 아티스트는 남자 그룹상, 여자 그룹상, 남자 가수상, 여자 가수상 총 4가지 부문의 후보들의 중심성 순위 평균을 비교해보았고, 프로듀서는 베스트 프로듀서 부문을 이용하였다. 그 결과 아티스트와 프로듀서 모두 가중연결 중심성(Weighted Degree Centrality)을 이용하는 것이 더 높은 정확성을 보였다. <br/>
인디 장르는 ‘한국대중음악상’의 최우수 모던록-노래와 음반 부문, 그리고 ‘멜론 뮤직 어워드’의 TOP10과 인디 부문 장르 상을 이용하여 적합한 중심성을 선정하였다. 이를 통하여 인디 부분에서도 가중연결 중심성(Weighted Degree Centrality)이 더 높은 정확도를 보여줌을 확인할 수 있었다.<br/><br/>

## 중심성 분석
### 힙합 분야
가중연결 중심성(Weighted Degree Centrality)을 이용하여 연도별로 중심성 상위권에 있는 힙합 아티스트들을 확인해보면 2가지 특징을 발견할 수 있었다. 첫 번째 특징은 해당 아티스트들의 차트인한 곡들은 셀프 프로듀싱하는 경우가 많다는 점이다. 그리고 또 다른 특징으로는 셀프 프로듀싱을 하지 않는 아티스트의 경우 작업을 자주 같이 진행하는 특정 프로듀서가 존재한다는 것이다.<br/>
매개 중심성(Betweenness Centrality)을 이용하여 연도별로 중심성 상위권인 힙합 프로듀서들을 확인해보았을 때도 마찬가지로 프로듀서들의 차트인 한 곡들은 같은 회사 소속의 아티스트와 작업한 경우가 많다는 것과, 아티스트 역할도 하는 프로듀서들은 셀프 프로듀싱을 한 곡들이 많이 차트인 했다는 점이다.
<br/><br/>
### 댄스 분야
다음으로는 가중연결 중심성(Weighted Degree Centrality)을 이용하여 댄스 분야의 아티스트와 프로듀서를 연도별로 상위권을 뽑아서 분석해보았다. 발견한 점은 아티스트와 프로듀서 모두 차트인 곡들을 보았을 때 주로 함께 작업하는 특정 프로듀서나 아티스트가 존재한다는 점이다.
<br/><br/>
### 인디 분야
마지막으로 가중연결 중심성(Weighted Degree Centrality)을 이용하여 인디 분야를 분석해본 결과 이전 힙합 분야와 마찬가지로 상위권의 아티스트와 프로듀서 모두 셀프 프로듀싱 하는 경우가 많고, 작업을 함께 하는 특정 프로듀서가 존재하였다.
<br/><br/>

## 신곡 추천 방식
신곡은 다음과 같은 기준으로 선별한다. 연도가 가까울수록 현재 영향력이 더 높다고 생각하기 때문에 공식을 (영향력) = [(2019년의 중심성)*0.2 + (2020년의 중심성)*0.3 + (2021년의 중심성) * 0.5]로 세웠다. 해당 식을 이용하여 아티스트나 프로듀서의 영향력을 계산한다. 해당 식에 대한 검증은 기존에 조사하였던 2019년부터 2021년까지의 데이터를 기반으로 2022년 1월부터 9월까지의 신곡들과 장르별 주간 차트를 이용하여 검증을 진행하였다.<br/>
힙합 분야에서 중심성 분석을 진행하였을 때 프로듀서는 매개 중심성(Betweenness Centrality)이 조금 더 적합하였다. 그러나 가중연결 중심성(Weighted Degree Centrality)과 점수 차이가 많이 나기 때문에 보정에 어려움이 있고, 가중연결 중심성(Weighted Degree Centrality)으로 분석하였을 때도 어느 정도 적합한 모습을 보여줬기 때문에 신곡 추천에서는 프로듀서 역시 가중연결 중심성(Weighted Degree Centrality)을 사용하였다.
<br/><br/>

## 신곡 추천 분석
### 힙합 분야
가중연결 중심성(Weighted Degree Centrality)을 이용한 분석 결과 발매 1,2주차를 기준으로 차트인 한 곡 중 예측하지 못한 곡은 77곡 중 6곡 밖에 없었다. 발매 이후 4주 차의 주간 차트 순위에서는 총 41곡 중 예측하지 못한 곡은 단 4곡밖에 없었다. 특히 예측한 37곡 중 30곡이 모두 중심성 수치가 1이 넘었다.<br/>
### 댄스 분야
댄스 분야를 가중연결 중심성(Weighted Degree Centrality)을 이용하여 분석 결과 총 107개의 차트인한 곡 중 84개의 곡을 선별하였으나, 84곡 중 중심성 수치가 1점 아래인 곡들이 49곡이나 되었다. 발매 4주 뒤 차트에서도 순위를 유지한 곡은 66곡이었으나 실제 예측은 48곡만 성공하였다. 그중 절반인 24곡이 1점 아래였다.<br/>
힙합 분야와 상대적으로 예측 정확도도 떨어지고 중심성 수치가 제대로 반영되지 않은 현상의 원인으로는 먼저 대형 신인 아이돌이 많이 나왔기 때문으로 보인다. 신인 아이돌은 최근 인기가 많더라도 지난 3년간의 데이터에 없을 가능성이 높고, 있더라도 중심성 수치가 낮을 것이다. 두 번째로는 솔로로 활동을 시작한 사람도 많다는 점이다. 기존의 그룹 활동이 아닌 솔로 활동한다면 지난 3년간의 데이터에 잡히지 않을 가능성이 높다.<br/>
### 인디 분야
인디 분야를 가중연결 중심성(Weighted Degree Centrality)을 이용하여 분석 결과 총 61개의 차트인한 곡 중 45개의 곡을 추천한 것으로 확인하였다. 그러나 추천곡들의 중심성 수치를 본다면 점수가 엄청 낮은 것을 알 수 있다. 45개의 곡 중 1점을 넘는 곡은 단 13곡밖에 되지 않는다. 발매 4주 이후의 주간 차트에서는 차트인 한 33곡 중 29곡을 예측하였다. 그러나 이 역시 1점을 넘는 곡은 10곡밖에 되지 않는다.<br/>
이러한 결과가 나온 이유로는 특정 사람들과 작업하는 경향이 인디 분야에서 특히 자주 도드라지기 때문이라고 생각한다. 특정 사람들이랑만 작업을 한다면 연결되는 노드가 제한적이기 때문에 가중연결 중심성(Weighted Degree Centrality) 수치는 낮아진다.<br/><br/>

## 결론 및 향후연구
### 결론
Graph Centrality 중 네 가지 중심성을 이용하여 적합한 중심성을 선정하였고 일반적으로 가중연결 중심성(Weighted Degree Centrality)이 좋은 효율을 보이고, 특정 조건에서는 다른 중심성을 이용하는 것이 더 좋은 효율을 보였다.<br/>
이후 해당 중심성을 바탕으로 분석을 진행한 결과 분야와 관계없이 차트인을 자주 하는 영향력 높은 아티스트나 프로듀서들은 함께 작업하는 특정 프로듀서나 아티스트가 존재한다는 공통적인 특징 발견할 수 있었다. 또 힙합 분야와 인디 분야에서 높은 영향력을 보이는 아티스트와 프로듀서는 셀프 프로듀싱을 하는 경우에 차트인하는 경우가 많다는 점 또한 알 수 있었다.<br/>
신곡 추천 과정에서는 모두 가중연결 중심성(Weighted Degree Centrality)을 이용하여 진행하였으며, 힙합 분야에서는 차트인할 곡을 매우 잘 예측하였으며 중심성 수치 역시 곡마다 적절하였다. 다른 분야에서는 중심성 수치는 부정확한 부분이 있었으나 힙합 분야만큼은 아니더라도 어느 정도 높은 예측률을 보여 주었다.<br/>

### 향후연구
향후 연구로는 새롭게 데뷔하는 아티스트나 프로듀서들에 대한 정보를 빠르게 반영하기 위하여 1년 단위로 데이터를 수집하는 것에서 반년이나 분기 단위로 데이터를 수집하는 것으로 변경하여 연구를 진행하는 것이다. 그렇게 한다면 댄스 분야에서 문제가 되었던 새롭게 데뷔하거나, 솔로 데뷔하는 사람들에 대한 부분들을 놓치지 않을 수 있을 것이다.<br/>
이 외에도 매개 중심성(Betweenness Centrality), 근접 중심성(Closeness Centrality), 가중연결 중심성(Weighted Degree Centrality), 고유벡터 중심성(Eigenvector Centrality) 네 가지 중심성뿐만 아니라 다른 중심성까지 확인해보아 댄스 분야나 인디 분야에 더욱 적합한 중심성을 찾는 연구도 진행할 수 있을 것이다.<br/>
<br/> 

## 참고문헌
[1] 조태수, 한치근, 이상훈, “그래프 중심성들을 이용한 그래프 유사도 측정”, 한국컴퓨터정보학회논문지, 2018.<br/>
[2] 김건희, 송근영, 한치근, “Graph Centrality를 이용한 국내 힙합 프로듀서와 아티스트 간 영향력과 음원 성적 분석”, 한국정보과학회 한국컴퓨터종합학술대회, 2022.<br/>
