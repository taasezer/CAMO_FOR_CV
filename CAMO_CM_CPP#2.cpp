#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdexcept>

extern "C" {
    __declspec(dllexport) void captureVideo() {
        try {
            cv::VideoCapture cap(0);
            if (!cap.isOpened()) {
                throw std::runtime_error("Kamera açılamadı!");
            }

            cv::Mat frame;
            while (true) {
                cap >> frame;
                if (frame.empty()) {
                    throw std::runtime_error("Boş frame alındı!");
                }

                cv::imshow("Kamera Görüntüsü", frame);
                if (cv::waitKey(1) == 'q') {
                    break;
                }
            }

            cap.release();
        } catch (const std::exception& e) {
            std::cerr << "Hata: " << e.what() << std::endl;
        }

        cv::destroyAllWindows();
    }
}
