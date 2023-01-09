const edit = document.querySelectorAll('button.btn-outline-secondary');
const save = document.querySelectorAll('button.btn-success');
const content = document.querySelectorAll('textarea.task-content');

/*
edit.forEach((item) => {
    item.addEventListener('click', toggleSaveBtn);
});
*/


edit.forEach((item, i) => {
    item.addEventListener('click', () => {
        if (save[i].style.visibility !== "visible") {
            console.log("hidden = false");
            save[i].style.visibility = "visible";
            content[i].readOnly = false;
        }
        else {
            console.log("hidden = true");
            save[i].style.visibility = "hidden";
            content[i].readOnly = true;
        }
    });

});

save.forEach((item, i) => {
    item.addEventListener('click', () => {
        console.log("save event")
        if (content[i].readOnly = false) {
            content[i].readOnly = true;
        }
        /*
        if (content[i].classList.contains('task-content')){

        }*/
    });
});
