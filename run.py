from flask import Flask,render_template,url_for,request,flash
from flask_mail import Mail,Message
import smtplib
from data import*






app=Flask(__name__)
active=True

app.config.update(
    DEBUG=True,
    MAIL_SERVER="mail.safehotelbd.com",
    MAIL_PORT=465,

    MAIL_USE_SSL=True,
    MAIL_USERNAME="order@safehotelbd.com",
    MAIL_PASSWORD="safehotelbd"
    )

app.config["SECRET_KEY"]="45y6hnbew54y6645ytu454e5ret"
mail=Mail(app)

@app.route("/")
def home():

    return render_template("home.html",active=active,
    couple_price=couple_price,
    super_price=super_price,
    double_price=double_price,
    dulex_price=dulex_price,
    single_price=single_price,
    good_single_price=good_single_price,
    good_double_price=good_double_price,
    good_couple_price=good_couple_price,

    couple_room_img=couple_room_img,
    double_room_img=double_room_img,
    single_room_img=single_room_img,
    dulex_room_img=dulex_room_img,
    super_room_img=super_room_img,
    good_single_room_img=good_single_room_img,
    good_double_room_img=good_double_room_img,
    good_couple_room_img=good_couple_room_img

)

@app.route("/about")
def about():
    return render_template("about.html",active=active)

@app.route("/rooms")
def rooms():
    return render_template("rooms.html",active=active,
            couple_price=couple_price,
            super_price=super_price,
            double_price=double_price,
            dulex_price=dulex_price,
            single_price=single_price,
            good_single_price=good_single_price,
            good_double_price=good_double_price,
            good_couple_price=good_couple_price,

            couple_room_img=couple_room_img,
            double_room_img=double_room_img,
            single_room_img=single_room_img,
            dulex_room_img=dulex_room_img,
            super_room_img=super_room_img,
            good_single_room_img=good_single_room_img,
            good_double_room_img=good_double_room_img,
            good_couple_room_img=good_couple_room_img
)
@app.route("/gallery")
def gallery():
    return render_template("gallery.html",active=active)



@app.route("/contact", methods=["GET","POST"])
def contact():
    ordr=[]
    if request.method=="POST":
        details=request.form
        for key,value in details.items():
            ordr.append(value)
        name=ordr[0]
        email=ordr[1]
        message=ordr[2]

    try:
        msg=Message("New mail from Go Safe Hotel Website",

                    sender="order@safehotelbd.com",
                    recipients=["zanjarwhite@gmail.com"])

        msg.body=("Name: "+name+"\nEmail: "+email+"\nMessage :"+message)
        mail.send(msg)
        flash("Thanks you,We got Information Successfully!")

    except Exception:
         pass


    return render_template("contact.html",active=active)


@app.route("/booking",methods=["GET","POST"])
def booking():
    bking=[]
    if request.method=="POST":
        booking=request.form
        for key,value in booking.items():
            bking.append(value)

        name=bking[0]
        email=bking[1]
        phone=bking[2]
        rmtype=bking[3]
        date=bking[4]
        message=bking[5]
    try:
        msg=Message("New Booking from Safe Hotel Website",
                    sender="order@safehotelbd.com",
                    recipients=["safehotelbd@gmail.com","pritomi.aakmam85@gmail.com"])

        msg.body=("Name: "+name+"\nEmail: "+email+"\nPhone :"+phone+"\nRoom Type: "+rmtype+"\nWish Date: "+date+"\nmessage: "+message)
        mail.send(msg)
        flash("We got your Booking Information Successfully")
    except Exception:
         pass

    return render_template("booking.html",room=["Super","Dulex","High Single","High Double","High Couple","Good Sinlge","Good Double","Good Couple"])


@app.route("/single")
def single():
    return render_template('single.html',
        single_price=single_price,
        single_room_img=single_room_img,
         single_details=single_details)

@app.route("/good_single")
def good_single():
    return render_template('good_single.html',
        good_single_price=good_single_price,
        good_single_room_img=good_single_room_img,
        good_single_details=good_single_details)

@app.route("/couple")
def couple():
    return render_template('couple.html',
    couple_price=couple_price,
    couple_room_img=couple_room_img,
    couple_details=couple_details)

@app.route("/good_couple")
def good_couple():
    return render_template('good_couple.html',
    good_couple_price=good_couple_price,
    good_couple_room_img=good_couple_room_img,
    good_couple_details=good_couple_details)

@app.route("/dulex")
def dulex():
    return render_template('dulex.html',
        dulex_price=dulex_price,
        dulex_room_img=dulex_room_img,
        dulex_details=dulex_details)

@app.route("/super")
def super():
    return render_template('super.html',
        super_price=super_price,
        super_room_img=super_room_img,
        super_details=super_details)

@app.route("/double")
def double():
    return render_template('double.html',
        double_price=double_price,
        double_room_img=double_room_img,
        double_details=double_details)
@app.route("/good_double")
def good_double():
    return render_template('good_double.html',
        good_double_price=good_double_price,
        good_double_room_img=good_double_room_img,
        good_double_details=good_double_details)

if __name__=="__main__":
    app.run(debug=True)
