#!/usr/bin/env python3
from app import app
from models import *

# alternative to flask shell
if __name__ == "__main__":
    with app.app_context():
        producer1 = Producer(
            name="Beckhams",
            founding_year=1889,
            region="Wales",
            operation_size="mega",
            image="beckhams.jpg",
        )

        import ipdb

        ipdb.set_trace()
