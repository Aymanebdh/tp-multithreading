#include <Eigen/Dense>
#include <cpr/cpr.h>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
  std::cout << "TP-4: Client C++ avec Eigen\n";

  std::cout << "\n=== 1. Test Eigen ===" << std::endl;
  Eigen::Matrix3d A;
  A << 1, 2, 3, 4, 5, 6, 7, 8, 9;
  Eigen::Vector3d b(1, 2, 3);

  std::cout << "Matrice A:\n" << A << std::endl;
  std::cout << "Vecteur b: " << b.transpose() << std::endl;

  std::cout << "\n=== 2. GET Task from proxy ===" << std::endl;
  auto get_resp = cpr::Get(cpr::Url{"http://localhost:8000/"});

  if (get_resp.status_code == 200) {
    auto task_json = json::parse(get_resp.text);
    std::cout << "Task size: " << task_json["size"] << std::endl;

    std::cout << "\n=== 3. POST Task to proxy ===" << std::endl;
    auto post_resp =
        cpr::Post(cpr::Url{"http://localhost:8000/"},
                  cpr::Header{{"Content-Type", "application/json"}},
                  cpr::Body{task_json.dump()});

    std::cout << "POST response: " << post_resp.text << std::endl;

    if (post_resp.status_code == 200) {
      std::cout << "\n SUCCÈS: C++/Python interop avec Eigen!" << std::endl;
    }
  }

  return 0;
}
