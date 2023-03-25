///이승현

//////////////////////////////////// 1번

// 느린 카운터를 만듭니다.
const counter_elem = document.getElementById("counter");
const btn = document.getElementById("btn");
const message = document.getElementById("message");

let click = 0;

const slowCounter = () => {
  const curClick = ++click;
  var counter = parseInt(counter_elem.innerText)
  message.innerHTML += `${curClick}. 현재 값은... ${counter}<br>`;

  window.setTimeout(() => {
    counter++
    counter_elem.innerText = counter
    message.innerHTML += `${curClick}. 더한 값은... ${counter}<br>`
  }, 3000);
};

btn.addEventListener("click", slowCounter);



///////////////////////////////////// 2번

function showInputWord() {
    const name = nameElem1.value
    instantShowElem.innerHTML = name
  }
  
  const nameElem1 = document.querySelector('#inputName1')
  const instantShowElem = document.querySelector('#instantShow')
  
  nameElem1.addEventListener("input", showInputWord) 
  
  
  /////////////////////////////////////////////////////
  
  function showInputWord2() {
    const name2 = nameElem2.value
    instantShowElem2.innerHTML = name2
  }
  
  const nameElem2 = document.querySelector('#inputName2')
  const instantShowElem2 = document.querySelector('#delayShow')
  
  nameElem2.addEventListener("input", () => {
      setTimeout(showInputWord2, 2000)
  }) 

  
  
 
  ///////////////////////////// 3번

  const btnSuccess = document.getElementById("btn_success");
const btnFail = document.getElementById("btn_fail");
const text = document.getElementById("text");

const prom = (param) => {
  return new Promise((resolve, reject) => {
      if (param) resolve(param = '성공')
      else reject(param = '실패')
    }
  );
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



//////////////////////////////////////// 4번

//1. `wait()`함수 내에 Promise를 생성합니다. 이때 `setTimeout()`이용해서 비동기 처리하세요.

function wait(time) {
    return new Promise((resolve, reject) => {
        setTimeout(function(){resolve()},time)
    });
  }
  
  //2. add()함수는 a,b 인자로 받은 두 가지 숫자의 합을 반환합니다.
  async function add(a, b) {
    return a+b;
  }
  
  //3. `calc()`함수는 `add()` 함수를 비동기처리해서 실행합니다. `await`을 사용해서 2초 후에 두 숫자의 합을 화면에 띄우세요.
  async function calc() {
    document.body.append("before wait")
    document.body.append(document.createElement("br"))
    var sum = await add(3,0)  
    await wait(2000)
    document.body.append("after wait")
    document.body.append(document.createElement("br"))
    document.body.append(`The sum is ${sum}`)
  }
  
  calc();
  
  



