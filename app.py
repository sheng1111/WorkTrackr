import sqlite3
from datetime import date, timedelta
from flask import Flask, render_template, request, redirect, g

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def close_db_connection(exception=None):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


def execute_query(query, params=None, fetchall=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    if fetchall:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()
    conn.commit()
    cursor.close()
    return result


def get_total_records_per_day(start_date, end_date):
    delta = end_date - start_date
    dates = [end_date - timedelta(days=i) for i in range(delta.days + 1)]
    total_records = []

    for date in dates:
        query = 'SELECT COUNT(*) FROM worktrackr WHERE date = ?'
        result = execute_query(query, (str(date),))
        total_records.append(result[0])

    return total_records


@app.route('/', methods=['GET'])
def home():
    end_date = date.today()
    start_date = end_date - timedelta(days=6)
    total_records_per_day = get_total_records_per_day(start_date, end_date)

    return render_template('index.html', total_records_per_day=total_records_per_day)


@app.route('/record')
def recordPage():
    return render_template('/record.html')


@app.route('/addRecord', methods=['GET', 'POST'])
def addRecord():
    if request.method == 'POST':
        date = request.form.get('date')
        period = request.form.get('period')
        taskType = request.form.get('taskType')
        taskName = request.form.get('taskName')
        status = request.form.get('status')
        note = request.form.get('note')
        remark = request.form.get('remark')

        query = 'INSERT INTO worktrackr (date, period, taskType, taskName, status, note, remark) VALUES (?, ?, ?, ?, ?, ?, ?)'
        execute_query(query, (date, period, taskType,
                      taskName, status, note, remark))

    return redirect('record')


@app.route('/todo')
def todoPage():
    query = 'SELECT * FROM todo ORDER BY date'
    todos = execute_query(query, fetchall=True)
    return render_template('todo.html', todos=todos)


@app.route('/addTodo', methods=['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        date = request.form.get('date')
        name = request.form.get('name')
        note = request.form.get('note')

        query = 'INSERT INTO todo (date, name, note) VALUES (?, ?, ?)'
        execute_query(query, (date, name, note))

    return redirect('todo')


@app.route('/deleteTodo', methods=['POST'])
def deleteTodo():
    if request.method == 'POST':
        todo_id = request.form.get('id')
        query = 'DELETE FROM todo WHERE id = ?'
        execute_query(query, (todo_id,))

    return redirect('todo')


@app.route('/search', methods=['GET', 'POST'])
def searchPage():
    records = []  # Define an initial value for 'records'

    if request.method == 'POST':
        # get_user_select
        date_filter = request.form.get('date_filter')
        customStartDate = str(request.form.get('startDate'))
        customEndDate = str(request.form.get('endDate'))

        if date_filter == 'today':
            start_date = date.today()
            end_date = date.today()
        elif date_filter == 'thisWeek':
            start_date = date.today() - timedelta(days=date.today().weekday())
            end_date = date.today()
        elif date_filter == 'thisMonth':
            start_date = date(date.today().year, date.today().month, 1)
            end_date = date.today()
        elif date_filter == 'custom':  # self_period
            start_date = customStartDate
            end_date = customEndDate
        else:
            start_date = date.today()
            end_date = date.today()

        query = 'SELECT * FROM worktrackr WHERE date BETWEEN ? AND ?'
        records = execute_query(
            query, (str(start_date), str(end_date)), fetchall=True)

    return render_template('search.html', records=records)


if __name__ == '__main__':
    app.run(port='9300', debug=True)
