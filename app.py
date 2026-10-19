from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-this-before-deploying')

# Demo data only. Replace these handlers with an officially supported Twist API
# integration before enabling real accounts, tasks, or redemptions.
DEMO = {
    'coins': 1250,
    'tasks': [
        {'id': 'listen', 'title': 'استمع إلى الموسيقى', 'description': 'استمع لمدة 10 دقائق', 'reward': 50, 'done': False},
        {'id': 'daily', 'title': 'المكافأة اليومية', 'description': 'افتح التطبيق يوميًا', 'reward': 25, 'done': True},
        {'id': 'playlist', 'title': 'اكتشف قائمة تشغيل', 'description': 'استكشف قائمة تشغيل جديدة', 'reward': 30, 'done': False},
    ],
    'packages': [
        {'code': 'small', 'name': 'باقة صغيرة', 'cost': 500, 'details': 'استبدال تجريبي'},
        {'code': 'medium', 'name': 'باقة متوسطة', 'cost': 1000, 'details': 'استبدال تجريبي'},
        {'code': 'large', 'name': 'باقة كبيرة', 'cost': 2000, 'details': 'استبدال تجريبي'},
    ],
}

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/dashboard')
def dashboard():
    return jsonify({'demo': True, 'coins': DEMO['coins'], 'tasks': DEMO['tasks'], 'packages': DEMO['packages']})

@app.post('/api/login/request-code')
def request_code():
    data = request.get_json(silent=True) or {}
    phone = str(data.get('phone', '')).strip()
    if not phone or len(phone) < 7:
        return jsonify({'error': 'اكتب رقم موبايل صحيحًا.'}), 400
    # Intentionally does not send a real SMS. Connect only to an authorized provider.
    return jsonify({'message': 'وضع تجريبي: لم يتم إرسال رسالة فعلية. اربط مزود OTP رسميًا لتفعيل الدخول.'})

@app.post('/api/login/verify')
def verify_code():
    # Do not collect or log real OTPs in a demo app.
    return jsonify({'error': 'التحقق الحقيقي غير مفعّل. يلزم ربط واجهة تسجيل دخول رسمية.'}), 501

@app.post('/api/tasks/<task_id>/claim')
def claim_task(task_id):
    task = next((t for t in DEMO['tasks'] if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'المهمة غير موجودة.'}), 404
    if not task['done']:
        task['done'] = True
        DEMO['coins'] += task['reward']
    return jsonify({'message': 'تم تحديث المهمة في العرض التجريبي فقط.', 'coins': DEMO['coins'], 'tasks': DEMO['tasks']})

@app.post('/api/redeem/<package_code>')
def redeem(package_code):
    package = next((p for p in DEMO['packages'] if p['code'] == package_code), None)
    if package is None:
        return jsonify({'error': 'الباقة غير موجودة.'}), 404
    if DEMO['coins'] < package['cost']:
        return jsonify({'error': 'رصيدك التجريبي لا يكفي.'}), 400
    # Demo only: no actual redemption is sent to Twist.
    DEMO['coins'] -= package['cost']
    return jsonify({'message': 'تم الاستبدال داخل العرض التجريبي فقط، ولم يتم تنفيذ استبدال حقيقي.', 'coins': DEMO['coins']})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
