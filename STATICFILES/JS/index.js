
const errorCont = document.getElementById('error')
if(errorCont.innerText !== ''){
    errorCont.classList.remove('hide')
    errorCont.classList.add('error')

    setTimeout(()=>{
        errorCont.classList.remove('error')
        errorCont.classList.add('hide')
    },6000)

}