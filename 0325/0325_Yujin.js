// 1.느린카운터

const counter = document.getElementById("counter");
const btn = document.getElementById("btn");
const message = document.getElementById("message");

let click = 0;

const slowCounter = () => {
  const curClick = ++click;
  let count = parseInt(counter.innerText)
  message.innerHTML += `${curClick}. 현재 값은... ${count}<br>`;

  window.setTimeout(() => {
    count++
    counter.innerHTML=count
    message.innerHTML += `${curClick}. 더한 값은... ${count}<br>`;
  }, 3000);
};

btn.addEventListener("click", slowCounter);








// 2.setTimeout 사용하여 웹 구현하기 2

// 입력 변화가 2초 뒤에 반영되는 코드를 작성해 보세요.
function showInputWord2() {
    const name = nameElem2.value
    setTimeout(()=>{delayShowElem.innerHTML = name},2000)
  }
  const nameElem2 = document.querySelector('#inputName2')
  const delayShowElem = document.querySelector('#delayShow')
  
  nameElem2.addEventListener("input", showInputWord2) 
  
  
  
  
  
  
  // 입력 변화가 바로 반영되는 코드는 아래와 같이 작성되어 있습니다.
  // 이를 참고하여, 위에, 입력 변화가 2초 뒤에 반영되는 코드를 작성해 보세요.
  function showInputWord() {
    const name = nameElem1.value
    instantShowElem.innerHTML = name
  }
  
  const nameElem1 = document.querySelector('#inputName1')
  const instantShowElem = document.querySelector('#instantShow')
  
  nameElem1.addEventListener("input", showInputWord) 








//   3.성공과 실패 버튼

const btnSuccess = document.getElementById("btn_success");
const btnFail = document.getElementById("btn_fail");
const text = document.getElementById("text");

const prom = (param) => {
  return new Promise((resolve,reject)=>{
        
            if (param){
                resolve("성공")
            }

            reject("실패")
    

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










// 4.wait 함수 만들기

//1. `wait()`함수 내에 Promise를 생성합니다. 이때 `setTimeout()`이용해서 비동기 처리하세요.

function wait(time) {
    return new Promise((resolve,reject) => {
        setTimeout(()=>resolve(),time)
    })
  }
  
  //2. add()함수는 a,b 인자로 받은 두 가지 숫자의 합을 반환합니다.
  async function add(a, b) {
  return a+b;
  }
  
  //3. `calc()`함수는 `add()` 함수를 비동기처리해서 실행합니다. `await`을 사용해서 2초 후에 두 숫자의 합을 화면에 띄우세요.
  async function calc() {
    document.body.append("before wait")
    await wait(2000)
    document.body.append(document.createElement("br"))
    document.body.append("after wait")
  
    const add1 = await add(1,2)
    document.body.append(document.createElement("br"))
    document.body.append("The sum is "+add1)
  }
  
  calc();
  
  
