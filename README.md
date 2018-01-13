# IBMCloud-python-flask

IBM Cloud python flask app sample


## Deployment to IBM Cloud

Web で tomcat の Cloud Foundry を生成してから、以下をやる。

    % bluemix api https://api.ng.bluemix.net
    % bluemix login -u <ログイン名> -o <組織名> -s <スペース名>
      (例: bluemix login -u hryuba@gmail.com -o hryuba@gmail.com -s dev)
    % bluemix app push <Cloud Foundry 登録名>

