const edit = document.querySelectorAll('button.btn-outline-secondary');
const save = document.querySelectorAll('button.btn-success');

/*
edit.forEach((item) => {
    item.addEventListener('click', toggleSaveBtn);
});
*/


edit.forEach((item, i) => {
    item.addEventListener('click', () => {
        if (save[i].hidden === true) {
            console.log("hidden = false");
            save[i].hidden = false;
        }
        else {
            console.log("hidden = true");
            save[i].hidden = true;
        }
    });

});
