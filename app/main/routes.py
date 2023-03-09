from datetime import datetime
from app import db, Config
from app.main import bp
from app.main.forms import EditProfileForm, PostForm
from flask import render_template, flash, redirect, url_for, current_app
from app.models import User, Post
from flask_login import current_user, login_required
from flask import request


@bp.route('/', methods=["GET", "POST"])
@bp.route('/main/index', methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Votre message est maintenant en ligne !")
        return redirect(url_for('main.index'))
    page = request.args.get(key='page', default=1, type=int)
    posts = current_user.posts_abonnes().paginate(page=page, max_per_page=current_app.config['POSTS_PAR_PAGE'], error_out=False)
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    return render_template('index.html', title='Accueil', form=form, posts=posts, prev_url=prev_url, next_url=next_url,size=Config.IMG_MAX_SIZE)


@bp.route('/main/explorer', methods=["GET"])
@login_required
def explorer():
    page = request.args.get(key='page', default=1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, max_per_page=current_app.config['POSTS_PAR_PAGE'],
                                                                error_out=False)
    prev_url = url_for('main.explorer', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.explorer', page=posts.next_num) if posts.has_next else None
    return render_template('index.html', title='Tous les messages présent sur le site', posts=posts, prev_url=prev_url,
                           next_url=next_url)


@bp.route('/main/apropos')
def apropos() -> str:
    return render_template('apropos.html')


@bp.route('/main/vhezronznzeomiezqjùpegnpqzeongezigqzipgnriogqnrgirngiqrngrino')
def disco() -> str:
    return render_template('baseMouvante.html')


@bp.route('/main/user/<username>')
@login_required
def user(username: str) -> str:
    page = request.args.get(key='page', default=1, type=int)
    user = User.query.filter(User.username == username).first_or_404('Accès refusé')
    posts = user.posts_abonnes().paginate(page=page, max_per_page=current_app.config['POSTS_PAR_PAGE'], error_out=False)
    prev_url = url_for('main.user', username=user.username, page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.user', username=user.username, page=posts.next_num) if posts.has_next else None
    return render_template('user.html', user=user, posts=posts, prev_url=prev_url, next_url=next_url)


@bp.route('/main/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Vos modification ont été enregistrées.')
        return redirect(url_for('main.user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/main/abonner/<username>')
@login_required
def abonner(username):
    user = User.query.filter(User.username == username).first()
    if user is None:
        flash(f"Erreur {username} non toruvé")
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(f"Erreur, vous ne pouvez pas vous abonner à vous même")
        return redirect(url_for('main.index'))
    current_user.abonner(user)
    db.session.commit()
    flash(f"Vous venez de vous abonner à {username}, vous pouvez maintenant voir ses posts")
    return redirect(url_for('main.user', username=username))


@bp.route('/main/desabonner/<username>')
@login_required
def desabonner(username: str):
    user = User.query.filter(User.username == username).first()
    if user is None:
        flash(f"L'utilisateur {username} n'a pas été trouvé.")
        return redirect(url_for('main.index'))
    if user == current_user:
        flash("Vous ne pouvez pas vous désabonner de vous-même.")
        return redirect(url_for('main.user'))
    current_user.desabonner(user)
    db.session.commit()
    flash(f"Vous êtes maintenant désabonné des messages de {username}.")
    return redirect(url_for('main.user', username=username))
