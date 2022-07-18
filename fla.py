from flask import Flask,request

app=Flask(__name__)
#/rout
@app.route('/webhook',methods=["GET","POST"])
def webhook():
    req=request.get_json(silent=True,force=True)
    fulfillmentText=""
    query_result=req.get("queryResult")
    if query_result.get("action")=="input.welcome":
        # do something
        # if required

        fulfillmentText="Hiya"
    return{
        "fulfillmentText": fulfillmentText,
        "source":"webhookdata"
        }
#running the app
if __name__=="__main__":
    app.run()
