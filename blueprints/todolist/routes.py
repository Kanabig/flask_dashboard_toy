from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_json, save_json, TODOLIST_FILE
from utils.timestamper import get_current_time_stamp_formated

todolist_bp = Blueprint(
    "todolist",
    __name__,
    url_prefix="/todolist",
)

# todolist main
@todolist_bp.route("/", methods=["GET"])
def todolist_service_main():
    return render_template("todolist/todolist_service_main.html")


# todo_write_form
@todolist_bp.route("/todo_write_form", methods=["GET"])
def todo_write_form():
    return render_template("todolist/todo_write_form.html")


# todo_write_confirm
@todolist_bp.route("/todo_write_confirm", methods=["GET"])
def todo_write_confirm():
    content = request.form["content"]
    expired_date = request.form["expired_date"]
    complete = request.form["complete"]

    mId = session["signinedMemberId"]

    todolists = load_json(TODOLIST_FILE)

    if mId in todolists:
        return render_template("todolist/todo_write_result.html", result="NG")

    todolists[mId] = [
        {
            "content": content,
            "expired_date": expired_date,
            "complete": complete,
            "reg_date": get_current_time_stamp_formated(),
            "mod_date": get_current_time_stamp_formated(),
        }
    ]

    save_json(TODOLIST_FILE, todolists)

    return render_template("todolist/todo_write_result.html", result="OK")


# todo_read_form ==========================================
@todolist_bp.route("/todo_read_form", methods=["GET"])
def todo_read_form():
    todolists = load_json(TODOLIST_FILE)
    todolist = todolists[session.get("signinedMemberId")]

    return render_template(
        'todo_read_form',
        todolist = todolist
    )


# todo_modify_form ==========================================
@todolist_bp.route("/todo_modify_form")
def todo_modify_form():
    todolists = load_json(TODOLIST_FILE)
    todolist = todolists[session.get("signinedMemberId")]

    return render_template(
        'todo_modify_form',
        todolist = todolist
    )

# todo_modify_confirm
@todolist_bp.route("/todo_modify_confirm")
def todo_modify_confirm():

    content = request.form["content"]
    expired_date = request.form["expired_date"]
    complete = request.form["complete"]

    todolists = load_json(TODOLIST_FILE)
    todolist = todolists['mId']
    todolist["content"] = content
    todolist["expired_date"] = expired_date
    todolist["complete"] = complete
    todolist["mod_date"] = get_current_time_stamp_formated()
    save_json(TODOLIST_FILE, todolist)

    return render_template("todo_modify_result.html")


# todo_delete_form
@todolist_bp.route("todo_delete_form", methods=["GET"])
def todo_delete_form():
    todolists = load_json(TODOLIST_FILE)
    todolist = todolists[session.get("signinedMemberId")]
    
    return render_template(
        'todo_delete_form',
        todolist = todolist
    )

# todo_delete_confirm
@todolist_bp.route("todo_delete_confirm", methods=["GET"])
def todo_delete_confirm():

    todolist = request.form["delete_index_number"]
 
    todolists = load_json(TODOLIST_FILE)
    del todolists[todolist]
    save_json(TODOLIST_FILE, todolists)

    render_template("todo_delete_result.html")
