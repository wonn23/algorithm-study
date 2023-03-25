// 0325 모의 테스트


////문제1 느린 카운터
// 느린 카운터를 만듭니다.
const counter = document.getElementById("counter");
const btn = document.getElementById("btn");
const message = document.getElementById("message");

let click = 0;

const slowCounter = () => {
  const curClick = ++click;
  const curValue = parseInt(counter.innerText);
  message.innerHTML += `${curClick}. 현재 값은... ${curValue}<br>`;

  window.setTimeout(() => {
    counter.innerText = curValue + 1;
    message.innerHTML += `${curClick}. 더한 값은... ${curValue+1}<br>`;
  }, 3000);
};

//innerText로 값을 바로 가져오고 초기화해야 숫자가 계속 늘어나는 불상사가 생기지 않는다... 하 어렵다

btn.addEventListener("click", slowCounter);


////문제2 setTimeout 사용하여 웹 구현하기 2
// 입력 변화가 2초 뒤에 반영되는 코드를 작성해 보세요.
function delayShow() {
    const name = nameElem2.value
    setTimeout(() => {
        delayShowElem.innerHTML = name
        }, 2000)
}

const nameElem2 = document.querySelector('#inputName2')
const delayShowElem = document.querySelector('#delayShow')

nameElem2.addEventListener("input", delayShow)



// 입력 변화가 바로 반영되는 코드는 아래와 같이 작성되어 있습니다.
// 이를 참고하여, 위에, 입력 변화가 2초 뒤에 반영되는 코드를 작성해 보세요.
function showInputWord() {
  const name = nameElem1.value
  instantShowElem.innerHTML = name
}

const nameElem1 = document.querySelector('#inputName1')
const instantShowElem = document.querySelector('#instantShow')

nameElem1.addEventListener("input", showInputWord) 



////문제3 성공과 실패 버튼

const btnSuccess = document.getElementById("btn_success");
const btnFail = document.getElementById("btn_fail");
const text = document.getElementById("text");

const prom = (param) => {
  return new Promise(function (resolve, reject) {
      if (param) {
          resolve('성공')
      }
      else {
          reject('실패')
      }
  });
};

btnSuccess.addEventListener("click", () => {
  prom(true).then(
    (param) => {
      text.innerText = `${param}했습니다!`;
    },
    (param) => {
      text.innerText = `${param}했습니다 ㅜㅜ`;
    }
  );
});

btnFail.addEventListener("click", () => {
  prom(false).then(
    (param) => {
      text.innerText = `${param}했습니다!`;
    },
    (param) => {
      text.innerText = `${param}했습니다 ㅜㅜ`;
    }
  );
});


////문제4 wait 함수 만들기
//1. `wait()`함수 내에 Promise를 생성합니다. 이때 `setTimeout()`이용해서 비동기 처리하세요.

function wait(time) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve();
        }, time)
    })
  }
  
  //2. add()함수는 a,b 인자로 받은 두 가지 숫자의 합을 반환합니다.
  async function add(a, b) {
    return a+b;
  }
  
  //3. `calc()`함수는 `add()` 함수를 비동기처리해서 실행합니다. `await`을 사용해서 2초 후에 두 숫자의 합을 화면에 띄우세요.
  async function calc() {
    document.body.append("before wait");
    document.body.append(document.createElement("br"));
    await wait(2000);
    document.body.append("after wait")
    document.body.append(document.createElement("br"));
    const result = await(add(1, 2))
    document.body.append(result);
  
  }
  
  calc();
  