from django import template

register = template.Library()

@register.inclusion_tag('hi-score/show_review.html')
def show_review(review, show_game_bool, cur_user):
    # show_game_bool determines whether the game name will show in the review
    return {'review': review, 'show_game_name':show_game_bool, 'user':cur_user}

