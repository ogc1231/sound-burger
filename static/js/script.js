let updateButtons = document.getElementsByClassName("add-to-cart")


for(let i =0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener("click", function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log("ProductId:", productId, "action:", action)
    })
}