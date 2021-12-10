# def encrypt(fn):
#     def wrapped():
#         if 'Секретные' in fn():
#             return '****** secret information ******'
#         return fn()
#     return wrapped
#
#
# @encrypt
# def get_secret_data():
#     return 'Секретные данные!'
#
# print(get_secret_data())


# def makeupper(fn):
#     def wrapped(name):
#         return fn(name).upper()
#     return wrapped
#
#
# # @makeupper
# def get_lower_name(name):
#     return name.lower()
#
# print(get_lower_name('ИгОрь'))


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())  ## выведет <b><i>hello habr</i></b>
