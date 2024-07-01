import reflex as rx


def nav() -> rx.Component:
    return rx.hstack(
        rx.heading("SaveDay"),
        rx.hstack(
            rx.text("Pricing", class_name="font-semibold text-xl"),
            rx.text("Blog", class_name="font-semibold text-xl"),
            rx.text("Help Center", class_name="font-semibold text-xl"),
            class_name="space-x-5",
        ),
        rx.hstack(
            rx.text(
                "Add to Chrome",
                class_name="font-semibold border-2 border-grey bg-gray-300 rounded-3xl p-3",
            ),
            rx.text(
                "Try Now",
                class_name="font-semibold border-2 border-grey bg-yellow-400 rounded-3xl p-3",
            ),
        ),
        class_name="border-2 border-grey rounded-full p-4 flex space-x-10 justify-around items-center mx-auto",
    )
