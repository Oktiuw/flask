from datetime import datetime

from app import app, db
from app.forms import EditProfileForm, PostForm
from flask import render_template, flash, redirect, url_for
from app.models import User, Post
from flask_login import current_user, login_required
from flask import request


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Votre message est maintenant en ligne !")
        return redirect(url_for('index'))
    page = request.args.get(key='page', default=1, type=int)
    posts = current_user.posts_abonnes().paginate(page=page, max_per_page=app.config['POSTS_PAR_PAGE'], error_out=False)
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    return render_template('index.html', title='Accueil', form=form, posts=posts, prev_url=prev_url, next_url=next_url)


@app.route('/explorer', methods=["GET"])
@login_required
def explorer():
    page = request.args.get(key='page', default=1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, max_per_page=app.config['POSTS_PAR_PAGE'], error_out=False)
    prev_url = url_for('explorer', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('explorer', page=posts.next_num) if posts.has_next else None
    return render_template('index.html', title='Tous les messages présent sur le site', posts=posts,prev_url=prev_url, next_url=next_url)


@app.route('/apropos')
def apropos() -> str:
    return render_template('apropos.html')


@app.route('/vhezronznzeomiezqjùpegnpqzeongezigqzipgnriogqnrgirngiqrngrino')
def disco() -> str:
    return render_template('baseMouvante.html')



@app.route('/user/<username>')
@login_required
def user(username: str) -> str:
    page = request.args.get(key='page', default=1, type=int)
    user = User.query.filter(User.username == username).first_or_404('Accès refusé')
    posts = user.posts_abonnes().paginate(page=page, max_per_page=app.config['POSTS_PAR_PAGE'], error_out=False)
    prev_url = url_for('user', username=user.username,page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('user', username=user.username,page=posts.next_num) if posts.has_next else None
    return render_template('user.html', user=user, posts=posts,prev_url=prev_url,next_url=next_url)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Vos modification ont été enregistrées.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/abonner/<username>')
@login_required
def abonner(username):
    user = User.query.filter(User.username == username).first()
    if user is None:
        flash(f"Erreur {username} non toruvé")
        return redirect(url_for('index'))
    if user == current_user:
        flash(f"Erreur, vous ne pouvez pas vous abonner à vous même")
        return redirect(url_for('index'))
    current_user.abonner(user)
    db.session.commit()
    flash(f"Vous venez de vous abonner à {username}, vous pouvez maintenant voir ses posts")
    return redirect(url_for('user', username=username))


@app.route('/desabonner/<username>')
@login_required
def desabonner(username: str):
    user = User.query.filter(User.username == username).first()
    if user is None:
        flash(f"L'utilisateur {username} n'a pas été trouvé.")
        return redirect(url_for('index'))
    if user == current_user:
        flash("Vous ne pouvez pas vous désabonner de vous-même.")
        return redirect(url_for('user'))
    current_user.desabonner(user)
    db.session.commit()
    flash(f"Vous êtes maintenant désabonné des messages de {username}.")
    return redirect(url_for('user', username=username))

