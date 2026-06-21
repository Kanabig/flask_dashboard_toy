function todo_write_form() {
    console.log('todo_write_form() Called');

    let form = document.todo_write_form;

    let content = form.content.value.trim();
    let expired_date = form.expired_date.value.trim();
    let complete = form.complete.value.trim();

    if (content === '') {
        alert('Please Input New Content');
        form.content.focus();

    } else if (expired_date === '') {
        alert('Please Select Expired_Date');
        form.expired_date.focus();

    } else if (complete === '') {
        alert('Please Select Complete or Not');
        form.complete.focus();

    } else {
        form.submit();
        
    }

}

function todo_modify_form() {
    console.log('todo_modify_form() CALLED!!');

    let form = document.todo_modify_form;

    let content = form.content.value.trim();
    let expired_date = form.expired_date.value.trim();
    let complete = form.complete.value.trim();

    if (content === '') {
        alert('Please Input New Content');
        form.content.focus();

    } else if (expired_date === '') {
        alert('Please Select Expired_Date');
        form.expired_date.focus();

    } else if (complete === '') {
        alert('Please Select Complete or Not');
        form.complete.focus();

    } else {
        form.submit();
        
    }

}
