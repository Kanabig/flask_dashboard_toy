function signupForm() {
  let form = document.signup_form;

  let id = form.mId.value.trim();
  let pw = form.mPw.value.trim();
  let mail = form.mMail.value.trim();
  let phone = form.mPhone.value.trim();

  if (id === "") {
    alert("please input id");
    form.mId.focus();
  } else if (pw === "") {
    alert("please input pw");
    form.mPw.focus();
  } else if (mail === "") {
    alert("please input mail");
    form.mMail.focus();
  } else if (phone === "") {
    alert("please input phone");
    form.mPhone.focus();
  } else {
    form.submit();
  }
}

function signInForm() {
  let form = document.signin_form;

  let id = form.mId.value.trim();
  let pw = form.mPw.value.trim();

  if (id === "") {
    alert("please input id");
    form.mId.focus();
  } else if (pw === "") {
    alert("please input pw");
    form.mPw.focus();
  } else {
    form.submit();
  }
}
