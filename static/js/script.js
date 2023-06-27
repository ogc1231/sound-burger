// let updateButtons = document.getElementsByClassName("add-to-cart")


// for(let i = 0; i < updateButtons.length; i++){
//     updateButtons[i].addEventListener('click', function(){
//         let productId = this.dataset.product
//         let action = this.dataset.action
//         console.log('productId:', productId, 'action:', action)

//         console.log('USER:', user)
//         // updateUserCart()
//     })
// }

// function updateUserCart(productId, action){
//     console.log('User is logged in')

//     let url = '/update_item/'

//     fetch(url, {
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body:JSON.stringify({'productId': productId, 'action': action})
//     })

//     .then((response) =>{
//         return response.json()
//         // return console.log(response)
//     })

//     .then((data) =>{
//         console.log('data:', data)
//         // location.reload()
//     })
// }