#include <gtk/gtk.h>

// callback function for button click event
void on_button_clicked(GtkWidget *widget, gpointer data) {
    g_print("Button clicked\n");
}

int main(int argc, char *argv[]) {
    GtkWidget *window, *button;
    gtk_init(&argc, &argv);
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    button = gtk_button_new_with_label("Click me");
    g_signal_connect(button, "clicked", G_CALLBACK(on_button_clicked), NULL);
    gtk_container_add(GTK_CONTAINER(window), button);
    gtk_widget_show_all(window);
    gtk_main();
    return 0;
}
