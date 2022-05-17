import datetime
import logging

import azure.functions as func
from . import momentum_list
from . import email

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    current_month_str = datetime.datetime.now().strftime("%B")
    current_year_str = datetime.datetime.now().strftime("%Y")
    print("generating list")
    generated_list = momentum_list.generate_momentum_list(debug=False)
    body = f"Please find below the updated mometum list for {current_month_str} {current_year_str}\n{generated_list}"
    email.send_email_custom(f"Momentum Rebalance {current_month_str} {current_year_str}", body)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)